


init -20 python:




    class Calendar(object):
        def __init__(self):
            self.appointments = {}
        
        
        def add(self, day, appointment):
            if day in self.appointments:
                self.appointments[day].append(appointment)
            else:
                self.appointments[day] = [appointment]
            NOTIFICATIONS.append(
            ["{image=gui/icons/icon_reminder.png}" + str(appointment.format(day)), 2]
        )
        
        def remove(self, day, appointment, cancelled=False, **kwargs):
            if day not in self.appointments:
                return
            if appointment in self.appointments[day]:
                if (
                cancelled
                and hasattr(appointment, "fail_label")
                and appointment.fail_label is not None
                and renpy.has_label(appointment.fail_label)
            ):
                    renpy.call_in_new_context(appointment.fail_label, from_cancel=True)
                self.appointments[day].remove(appointment)
        
        def find_and_remove(self, **kwargs):
            for day, appointment in self.find(**kwargs):
                self.remove(day, appointment, **kwargs)
        
        def find(self, **kwargs):
            retval = []
            for day, appointments in self.appointments.items():
                for appointment in appointments:
                    if appointment.find(**kwargs):
                        retval.append((day, appointment))
            return retval
        
        def has_date(self, day=None, hour=None, girl=None):
            if day is None:
                day = game.days_played
            if hour is None:
                hour = game.hour
            
            if not self.appointments.get(day):
                return False
            
            for appointment in self.appointments[day]:
                if (
                isinstance(appointment, (DateAppointment, HaremAppointment))
                and appointment.is_available(hour)
                and (girl is None or appointment.find(girl=girl))
            ):
                    return True
            return False
        
        def has_appointment(self, day=None, hour=None, girl=None):
            if day is None:
                day = game.days_played
            if hour is None:
                hour = game.hour
            
            if not self.appointments.get(day):
                return False
            
            for appointment in self.appointments[day]:
                if (
                not isinstance(appointment, (DateAppointment, HaremAppointment))
                and appointment.is_available(hour)
                and (girl is None or appointment.find(girl=girl))
            ):
                    return True
            return False
        
        def get_appointments(self, day=None, hour=None, girl=None):
            retval = []
            
            if day is None:
                day = game.days_played
            if hour is None:
                hour = game.hour
            
            if self.appointments.get(day):
                for appointment in self.appointments[day]:
                    if appointment.is_available(hour) and (
                    girl is None or appointment.find(girl=girl)
                ):
                        if isinstance(appointment, DateEvent):
                            for p in appointment.participants:
                                if not Person.find(p):
                                    continue
                        retval.append(appointment)
            return retval
        
        def clean_up(self):
            
            old_days = [d for d in self.appointments if d < game.days_played]
            for old_day in old_days:
                for appointment in self.appointments[old_day]:
                    appointment.fail()
                del self.appointments[old_day]
            
            for hidden_person in Person.all_hidden_people():
                if self.find(npc=hidden_person.id):
                    renpy.log(f"Deleting appointment for hidden person {hidden_person.id}")
                    self.find_and_remove(npc=hidden_person.id)
        
        def get_agenda(self):
            """
        Builds a list of items for rendering in the smartphone Calendar display.
        Build the initial list based on known birthdays and not hidden characters, constrained to 14 days.
        This should maybe use something other than hidden (like a universal 'started' or 'met' flag)?
        """
            agenda = [
            (
                (game.calendar.get_future_days_played(*person.birthday), -1),
                AgendaEntry(
                    game.calendar.get_future_day_of_week_name(
                        *person.birthday, short=True
                    ).capitalize(),
                    "All Day",
                    "Birthday (" + person.name + ")",
                ),
            )
            for person in Person.all_people(ignore_hidden=True)
            if person.flags.birthdayknown
            and game.calendar.get_future_days_played(*person.birthday)
            - game.days_played
            < 7
        ]
            
            for day, appointments in self.appointments.items():
                for appointment in appointments:
                    try:
                        agenda.append(
                        ((day, int(appointment.hour)), appointment.format(day))
                    )
                    except ValueError:
                        del self.appointments[day]
            
            
            
            return [
            entry
            for _, entry in sorted(agenda, key=lambda e: (e[0][0], e[0][1], e[1].name))
        ]
        
        def get_agenda_day(self, day=None):
            if day is None:
                day = game.days_played
            agenda = []
            if day in self.appointments:
                for appointment in sorted(self.appointments[day], key=lambda x: x.hour):
                    agenda.append(appointment.format(day))
            return agenda



    class Appointment(object):
        def __init__(self, hours, name, fixed_hour=False):
            
            if isinstance(hours, int) and hours < 22:
                hours = (hours, hours + 2)
            
            self.hours = (hours, hours) if isinstance(hours, int) else hours
            self.hour = self.hours[0]
            self.name = name
            self.fixed_hour = fixed_hour
        
        def do(self):
            
            raise NotImplementedError
        
        def fail(self):
            
            raise NotImplementedError
        
        def find(self, **kwargs):
            
            raise NotImplementedError
        
        def is_available(self, hour):
            if isinstance(self.hours, int):
                return self.hours == hour
            elif isinstance(self.hours, tuple) or isinstance(self.hours, list):
                if self.hours[0] <= self.hours[1]:
                    return self.hours[0] <= hour <= self.hours[1]
                else:
                    return hour >= self.hours[0] or hour <= self.hours[1]
            return False
        
        
        
        def format(self, day):
            day = game.calendar.get_future_day_of_week_name(day, short=True).capitalize()
            if not isinstance(self.hours, int) and self.hours[0] != self.hours[1]:
                return AgendaEntry(
                day=day, hour=f"{self.hours[0]}:00 - {self.hours[1]}:00", name=self.name
            )
            else:
                return AgendaEntry(day=day, hour=f"{self.hour}:00", name=self.name)


    class AgendaEntry(NoRollback):
        def __init__(self, day, hour, name):
            self.day = day
            self.hour = hour
            self.name = name
        
        def __str__(self):
            return f"{self.day} {self.hour} {self.name}"
        
        def __repr__(self):
            return f"{self.day} {self.hour} {self.name}"
        
        def format(self, day):
            day = game.calendar.get_future_day_of_week_name(day, short=True).capitalize()
            return AgendaEntry(day=day, hour=str(self.hour) + ":00", name=self.name)


    class ReminderAppointment(Appointment):
        def __init__(self, hours, name, label, fixed_hour=False):
            Appointment.__init__(self, hours, name, fixed_hour)
            self.label = label
        
        def do(self):
            pass
        
        def fail(self):
            pass
        
        def find(self, **kwargs):
            if "label" not in kwargs:
                return False
            if "label" in kwargs and self.label != kwargs["label"]:
                return False
            return True


    class LabelAppointment(Appointment):
        def __init__(
        self, hours, participants, name, label, fail_label=None, fixed_hour=False
    ):
            if participants is None:
                participants = []
            elif isinstance(participants, basestring):
                participants = [participants]
            elif isinstance(participants, tuple):
                participants = list(participants)
            Appointment.__init__(self, hours, name, fixed_hour)
            self.label = label
            self.participants = participants
            self.fail_label = fail_label
        
        def _m1_class_appointment__participant_names(self):
            return ", ".join(Person.find(x).name for x in self.participants)
        
        def do(self):
            if self.label not in DONE_HOUR:
                DONE_HOUR.append(self.label)
            DONE[self.label] = game.days_played
            return self.label
        
        def fail(self):
            if self.fail_label is not None and renpy.has_label(self.fail_label):
                renpy.call_in_new_context(self.fail_label)
        
        def find(self, **kwargs):
            if "label" not in kwargs and "girl" not in kwargs and "npc" not in kwargs:
                return False
            if "label" in kwargs and self.label != kwargs["label"]:
                return False
            if "girl" in kwargs and not kwargs["girl"] in self.participants:
                return False
            if "npc" in kwargs and not kwargs["npc"] in self.participants:
                return False
            if "date_only" in kwargs and not isinstance(
            self, (DateAppointment, HaremAppointment)
        ):
                return False
            return True
        
        def __setstate__(self, state_dict):
            self.__dict__ = state_dict
            
            if hasattr(self, "girls"):
                self.participants = self.girls
                delattr(self, "girls")


    class HaremAppointment(LabelAppointment):
        def __init__(
        self,
        hours,
        harem,
        participants,
        label,
        name=None,
        fail_label=None,
        fixed_hour=False,
    ):
            LabelAppointment.__init__(
            self, hours, participants, name, label, fail_label, fixed_hour
        )
            if not name:
                self.name = "Harem Date: (" + self._m1_class_appointment__participant_names() + ")"
            self.harem = harem  
        
        def find(self, **kwargs):
            if "harem" in kwargs and not self.harem == kwargs["harem"]:
                return False
            return LabelAppointment.find(self, **kwargs)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
