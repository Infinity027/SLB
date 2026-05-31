init -20:
    define JOBS = {}
    default AVAILABLE_JOBS = {}
    default DONE_JOBS = {}

init python:
    DayTransitionEvent(**{
    "name": "career_daily",
    "label": "career_daily",
    "priority": 1000,
    })

    DayTransitionEvent(**{
    "name": "career_weekly",
    "label": "career_weekly",
    "conditions": [
        IsDayOfWeek("5"),
        ],
    "priority": 999,
    "once_day": False,
    "once_week": True,
    })

label career_daily:
    python:
        for g in Person.all_people():
            if g.flags.career and not g.flags.noprocesscareer and g.flags.job and g.flags.job in AVAILABLE_JOBS[g.id]:
                career_daily_girl(g)
    return

label career_weekly:
    python:
        for g in Person.all_people():
            if g.flags.career and not g.flags.noprocesscareer:
                career_weekly_girl(g)
    return

label smartphone_look_for_jobs(girl):


    python:


        renpy.dynamic("old_active_girl")
        old_active_girl = active_girl.object
        active_girl.object = girl
        renpy.dynamic('name', 'job', 'foundone')
        if not DONE_JOBS.get(girl.id):
            DONE_JOBS[girl.id] = []
        foundone = False
        for name, job in JOBS.items():
            if name not in DONE_JOBS[girl.id] and job.test():
                renpy.call_in_new_context(job.label)
                DONE_JOBS[girl.id].append(name)
                foundone = True

        if not foundone:
            renpy.say("", "I call everyone I can think of, but there aren't any new jobs available.")

        active_girl.object = old_active_girl
    return

label smartphone_set_job(girl, job):
    $ girl.flags.job = job
    if renpy.has_label(girl.id + "_new_job"):
        call expression f"{girl.id}_new_job" pass (JOBS[job]) from _call_expression_515
    return

label job_add(girl, job):
    if not AVAILABLE_JOBS.get(girl):
        $ AVAILABLE_JOBS[girl] = []
    if job not in AVAILABLE_JOBS[girl]:
        $ AVAILABLE_JOBS[girl].append(job)
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
