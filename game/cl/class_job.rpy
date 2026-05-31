
init -20 python:



    class Job(Conditioned):
        def __init__(
        self,
        id,
        name,
        description,
        label,
        income,
        career_gain,
        career_max,
        difficulty=0,
        conditions=None,
    ):
            super(Job, self).__init__(id, conditions)
            
            self.name = name
            self.description = description
            self.label = label
            self.income = income
            self.career_gain = career_gain
            self.career_max = career_max
            self.difficulty = difficulty
            
            JOBS[self.id] = self



init python:



    def career_daily_girl(girl):
        job = JOBS.get(girl.flags.job)
        if not job or girl.career > job.career_max:
            return
        
        if isinstance(job.career_gain, tuple):
            if not str(game.week_day) in job.career_gain[1]:
                return
            gain = job.career_gain[0]
        else:
            gain = job.career_gain
        
        if debug:
            renpy.log(gain)
        max_gain = job.career_max - girl.career
        girl.career += min(gain, max_gain)
        if renpy.has_label(girl.id + "_career_daily"):
            renpy.call(girl.id + "_career_daily")
        return


    def career_weekly_girl(npc):
        if renpy.has_label(npc.id + "_career_weekly"):
            retval = renpy.call(npc.id + "_career_weekly")
        
        
        job = JOBS.get(npc.flags.job)
        
        expenses = npc.flags.jobexpenses
        loan = npc.flags.jobloan
        if job:
            message = f"{npc.name} got paid {job.income}{{image=gui/icons/icon_money.png}}."
        else:
            message = f"{npc.name} is unemployed this week."
        
        if npc.is_male:
            pronoun = "his"
        else:
            pronoun = "her"
        
        loanpayment = 0
        if expenses > 0:
            message += f" {pronoun.capitalize()} weekly expenses are {expenses}{{image=gui/icons/icon_money.png}}."
        if loan > 0:
            loanpayment = min(loan, npc.flags.jobloanmax or 250)
            message += f" {pronoun.capitalize()} loan payment is {loanpayment}{{image=gui/icons/icon_money.png}}."
            npc.flags.jobloan = max(0, loan - loanpayment)
            if loan - loanpayment > 0:
                message += (
                f" ({loan - loanpayment}){{image=gui/icons/icon_money.png}} remains)"
            )
            else:
                message += f" {pronoun.capitalize()} loan is now paid off!"
        
        if job:
            income = job.income - expenses - loanpayment
        else:
            income = 0 - expenses - loanpayment
        
        if income >= 0:
            agent_cut = int(floor(income * 0.1))
            message += f" {pronoun.capitalize()} net income is {income}{{image=gui/icons/icon_money.png}} and my cut of that is {agent_cut}{{image=gui/icons/icon_money.png}}."
            hero.money += agent_cut
        else:
            message += f" {pronoun.capitalize()} income does not cover {pronoun} expenses, so I have to make up the shortfall of {income}{{image=gui/icons/icon_money.png}}."
            hero.money += income
        if job and job.career_max <= npc.career < 100:
            message += f" {pronoun.capitalize()} career will no longer advance at this job."
        renpy.say("", message)
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
