import datetime
import random
import os

today = datetime.date.today()
day_of_year = today.timetuple().tm_yday
weekday = today.strftime("%A")
date_str = today.strftime("%B %d, %Y")

quotes = [
    "\"First, solve the problem. Then, write the code.\" — John Johnson",
    "\"Clean code always looks like it was written by someone who cares.\" — Robert C. Martin",
    "\"Any fool can write code that a computer can understand. Good programmers write code that humans can understand.\" — Martin Fowler",
    "\"Make it work, make it right, make it fast.\" — Kent Beck",
    "\"The best error message is the one that never shows up.\" — Thomas Fuchs",
    "\"Simplicity is the soul of efficiency.\" — Austin Freeman",
    "\"Code is like humor. When you have to explain it, it's bad.\" — Cory House",
    "\"Programming is the art of telling another human what one wants the computer to do.\" — Donald Knuth",
    "\"The most dangerous phrase in the language is: We have always done it this way.\" — Grace Hopper",
    "\"Talk is cheap. Show me the code.\" — Linus Torvalds",
]

tips = [
    "Tip: Write tests before you write code (TDD).",
    "Tip: Commit early, commit often — small commits are easier to review.",
    "Tip: Name variables for what they represent, not how they are used.",
    "Tip: A function should do one thing and do it well.",
    "Tip: Read other people's code — it's the fastest way to improve.",
    "Tip: Always handle edge cases — they will happen in production.",
    "Tip: Document the 'why', not the 'what' — code shows the what.",
    "Tip: Use version control for everything, even solo projects.",
    "Tip: Learn to use the debugger properly — console.log only goes so far.",
    "Tip: Take breaks — your best ideas come away from the screen.",
    "Tip: Understand the problem completely before writing a single line of code.",
    "Tip: Refactor regularly — technical debt compounds like interest.",
]

random.seed(day_of_year)
quote = random.choice(quotes)
tip = random.choice(tips)

log_file = "dev-log.md"

if not os.path.exists(log_file):
    with open(log_file, "w") as f:
        f.write("# 📓 Dev Log — Jeeban Mohanty\n\n")
        f.write("> A daily log of coding, learning, and building.\n\n")
        f.write("---\n\n")

with open(log_file, "r") as f:
    existing = f.read()

entry = f"""## {date_str} ({weekday})

> {quote}

**{tip}**

---

"""

# Insert after header (after first ---)
insert_pos = existing.find("---\n\n") + len("---\n\n")
new_content = existing[:insert_pos] + entry + existing[insert_pos:]

with open(log_file, "w") as f:
    f.write(new_content)

print(f"[+] Dev log updated for {date_str}")
