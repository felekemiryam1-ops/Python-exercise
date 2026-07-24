from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT

OUTPUT = "/sessions/eager-tender-hopper/mnt/outputs/Cloud_Engineer_Academy_Study_Guide.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=letter,
    rightMargin=0.75*inch,
    leftMargin=0.75*inch,
    topMargin=0.75*inch,
    bottomMargin=0.75*inch,
)

styles = getSampleStyleSheet()

# ── Custom styles ──────────────────────────────────────────────────────────────
NAVY   = colors.HexColor("#1a2b4a")
TEAL   = colors.HexColor("#0d7377")
GOLD   = colors.HexColor("#f4a261")
LIGHT  = colors.HexColor("#f0f4f8")
WHITE  = colors.white
GREEN  = colors.HexColor("#2d6a4f")
RED    = colors.HexColor("#9b2226")

def S(name, **kw):
    return ParagraphStyle(name, **kw)

cover_title  = S("CoverTitle",  fontSize=32, textColor=WHITE, alignment=TA_CENTER, fontName="Helvetica-Bold", spaceAfter=6)
cover_sub    = S("CoverSub",    fontSize=16, textColor=GOLD,  alignment=TA_CENTER, fontName="Helvetica-Bold", spaceAfter=4)
cover_body   = S("CoverBody",   fontSize=11, textColor=WHITE, alignment=TA_CENTER, fontName="Helvetica",      spaceAfter=4)
mod_header   = S("ModHeader",   fontSize=18, textColor=WHITE, fontName="Helvetica-Bold", spaceAfter=4, spaceBefore=4)
section_head = S("SectionHead", fontSize=13, textColor=NAVY,  fontName="Helvetica-Bold", spaceAfter=4, spaceBefore=10, borderPad=2)
body         = S("Body",        fontSize=10, textColor=colors.black, fontName="Helvetica", leading=15, spaceAfter=3)
bullet_style = S("Bullet",      fontSize=10, textColor=colors.black, fontName="Helvetica", leading=14, leftIndent=16, firstLineIndent=-10, spaceAfter=2)
q_style      = S("QStyle",      fontSize=10, textColor=NAVY,  fontName="Helvetica-Bold", leading=14, spaceAfter=2, spaceBefore=6)
a_style      = S("AStyle",      fontSize=10, textColor=GREEN, fontName="Helvetica",      leading=14, spaceAfter=4, leftIndent=12)
deadline_sty = S("Deadline",    fontSize=10, textColor=RED,   fontName="Helvetica-Bold", spaceAfter=2)
outcome_sty  = S("Outcome",     fontSize=10, textColor=GREEN, fontName="Helvetica",      leading=14, leftIndent=16, firstLineIndent=-10, spaceAfter=2)

story = []

# ══════════════════════════════════════════════════════════════════════════════
# COVER PAGE
# ══════════════════════════════════════════════════════════════════════════════
def cover_table():
    data = [[
        Paragraph("CLOUD ENGINEER ACADEMY", cover_title),
    ],[
        Paragraph("Complete Study Guide", cover_sub),
    ],[
        Paragraph("Late July – December 2026", cover_sub),
    ],[
        Spacer(1, 14),
    ],[
        Paragraph("Python  •  AWS Cloud Practitioner  •  AWS Solutions Architect", cover_body),
    ],[
        Paragraph("Terraform  •  Docker  •  Kubernetes  •  CI/CD  •  GlamCloud AI MVP", cover_body),
    ],[
        Spacer(1, 20),
    ],[
        Paragraph("Every module includes: learning objectives · projects with deadlines · mock interview Q&amp;A", cover_body),
    ]]
    t = Table(data, colWidths=[6.5*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0,0), (-1,-1), NAVY),
        ("ALIGN",       (0,0), (-1,-1), "CENTER"),
        ("VALIGN",      (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING",  (0,0), (-1,-1), 6),
        ("BOTTOMPADDING",(0,0),(-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 16),
        ("RIGHTPADDING",(0,0), (-1,-1), 16),
        ("ROWBACKGROUNDS",(0,0),(-1,-1),[NAVY]),
    ]))
    return t

story.append(Spacer(1, 0.8*inch))
story.append(cover_table())
story.append(Spacer(1, 0.3*inch))

# Overview table
overview_data = [
    ["PHASE", "DATES", "PRIMARY FOCUS", "MILESTONE"],
    ["1 – Foundations", "Jul 22–31", "Python + Git + Linux", "GitHub active"],
    ["2 – AWS Practitioner", "August", "Python Intermediate + AWS CLF", "Pass AWS Cloud Practitioner"],
    ["3 – AWS Architect", "September", "AWS SAA + GlamCloud Start", "Pass SAA by Sep 30 + Begin GlamCloud AI"],
    ["4 – IaC", "October", "Terraform + Git/GitHub", "Resume + LinkedIn + Apply"],
    ["5 – Containers", "November", "Docker + Linux + CI/CD", "10+ applications/week"],
    ["6 – Orchestration", "December", "Kubernetes + Security + Jobs", "GlamCloud MVP + Hired"],
]
ov_table = Table(overview_data, colWidths=[1.3*inch, 1.1*inch, 2.2*inch, 1.9*inch])
ov_table.setStyle(TableStyle([
    ("BACKGROUND",  (0,0), (-1,0), TEAL),
    ("TEXTCOLOR",   (0,0), (-1,0), WHITE),
    ("FONTNAME",    (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",    (0,0), (-1,-1), 9),
    ("FONTNAME",    (0,1), (-1,-1), "Helvetica"),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[LIGHT, WHITE]),
    ("ALIGN",       (0,0), (-1,-1), "CENTER"),
    ("VALIGN",      (0,0), (-1,-1), "MIDDLE"),
    ("GRID",        (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
    ("TOPPADDING",  (0,0), (-1,-1), 5),
    ("BOTTOMPADDING",(0,0),(-1,-1), 5),
]))
story.append(ov_table)
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════
def module_banner(title, subtitle):
    data = [[Paragraph(title, mod_header)],[Paragraph(subtitle, cover_body)]]
    t = Table(data, colWidths=[6.5*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0,0), (-1,-1), NAVY),
        ("LEFTPADDING", (0,0), (-1,-1), 14),
        ("RIGHTPADDING",(0,0), (-1,-1), 14),
        ("TOPPADDING",  (0,0), (-1,-1), 8),
        ("BOTTOMPADDING",(0,0),(-1,-1), 8),
    ]))
    return t

def section_box(title):
    data = [[Paragraph(title, section_head)]]
    t = Table(data, colWidths=[6.5*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0,0), (-1,-1), LIGHT),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING",  (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0),(-1,-1), 4),
        ("LINEBELOW",   (0,0), (-1,-1), 1.5, TEAL),
    ]))
    return t

def bullet(text):
    return Paragraph(f"• {text}", bullet_style)

def outcome(text):
    return Paragraph(f"✓  {text}", outcome_sty)

def deadline(text):
    return Paragraph(f"⏰  DEADLINE: {text}", deadline_sty)

def q(text):
    return Paragraph(f"Q: {text}", q_style)

def a(text):
    return Paragraph(f"A: {text}", a_style)

def project_table(rows):
    data = [["#", "PROJECT", "DEADLINE", "DELIVERABLE"]] + rows
    t = Table(data, colWidths=[0.3*inch, 2.1*inch, 1.4*inch, 2.7*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0,0), (-1,0), TEAL),
        ("TEXTCOLOR",   (0,0), (-1,0), WHITE),
        ("FONTNAME",    (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",    (0,0), (-1,-1), 9),
        ("FONTNAME",    (0,1), (-1,-1), "Helvetica"),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[LIGHT, WHITE]),
        ("ALIGN",       (0,0), (-1,-1), "LEFT"),
        ("VALIGN",      (0,0), (-1,-1), "TOP"),
        ("GRID",        (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
        ("TOPPADDING",  (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0),(-1,-1), 4),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
    ]))
    return t

# ══════════════════════════════════════════════════════════════════════════════
# MODULE 1: Late July — Python Foundations + Git + Linux
# ══════════════════════════════════════════════════════════════════════════════
story.append(module_banner(
    "MODULE 1: Python Foundations + Git + Linux",
    "Late July 2026  |  July 22 – July 31  |  10 Days"
))
story.append(Spacer(1, 10))

story.append(section_box("Overview"))
story.append(Paragraph(
    "You're launching the academy today. This first sprint is about building momentum and good habits. "
    "You will set up your development environment, write your first Python programs, learn the Linux "
    "terminal, and make your GitHub profile active. Every day counts — commit code every single day.",
    body))

story.append(section_box("Daily Schedule  (3–4 hrs)"))
sched_data = [
    ["TIME", "ACTIVITY"],
    ["8:00–9:30 AM", "Python study (new concept + notes)"],
    ["9:30–9:45 AM", "Break"],
    ["9:45–11:15 AM", "Python coding practice / mini lab"],
    ["11:15–11:45 AM", "Linux terminal practice OR Git/GitHub"],
    ["Evening (optional)", "30 min review, GitHub commit, journal entry"],
]
s_table = Table(sched_data, colWidths=[1.8*inch, 4.7*inch])
s_table.setStyle(TableStyle([
    ("BACKGROUND",  (0,0), (-1,0), TEAL),
    ("TEXTCOLOR",   (0,0), (-1,0), WHITE),
    ("FONTNAME",    (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",    (0,0), (-1,-1), 9),
    ("FONTNAME",    (0,1), (-1,-1), "Helvetica"),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[LIGHT, WHITE]),
    ("GRID",        (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
    ("TOPPADDING",  (0,0), (-1,-1), 4),
    ("BOTTOMPADDING",(0,0),(-1,-1), 4),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
]))
story.append(s_table)
story.append(Spacer(1, 6))

story.append(section_box("Topics to Cover"))
for t in [
    "Python: variables, data types (int, float, str, bool), print statements, input()",
    "Python: if/elif/else, comparison operators, logical operators",
    "Python: for loops, while loops, range()",
    "Python: functions — def, parameters, return values",
    "Python: lists — indexing, slicing, append, remove, iteration",
    "Python: dictionaries — key/value pairs, get, update, iteration",
    "Linux: ls, cd, mkdir, rm, cp, mv, cat, echo, pwd, man",
    "Linux: file permissions (chmod), nano/vim basics",
    "Git: init, add, commit, push, pull, clone, status, log",
    "GitHub: create repo, write a README.md, push from terminal",
]:
    story.append(bullet(t))
story.append(Spacer(1, 6))

story.append(section_box("Projects + Deadlines"))
story.append(project_table([
    ["1", "BMI Calculator", "July 26", "Python script that takes height/weight, calculates BMI, prints category"],
    ["2", "Password Generator", "July 31", "Python script using random module; lets user choose length and complexity"],
]))
story.append(deadline("Both projects pushed to GitHub with README by July 31"))
story.append(Spacer(1, 6))

story.append(section_box("What You Should Know by the End of Module 1"))
for o in [
    "Write a Python script from scratch using variables, loops, functions, and lists",
    "Explain the difference between a list and a dictionary",
    "Navigate the Linux file system using the terminal without looking anything up",
    "Create a GitHub repo, add files, and push commits from the command line",
    "Explain what Git is and why version control matters",
]:
    story.append(outcome(o))
story.append(Spacer(1, 8))

story.append(section_box("Mock Interview — Module 1"))
story.append(q("What is the difference between a list and a dictionary in Python?"))
story.append(a("A list is an ordered collection accessed by index (list[0]). A dictionary is an unordered collection of key-value pairs accessed by key (dict['name']). Use a list when order matters; use a dict when you need to label your data."))
story.append(q("What does the 'def' keyword do in Python?"))
story.append(a("It defines a function. You give the function a name, optional parameters, and a body. Functions allow you to write reusable, organized code rather than repeating the same logic multiple times."))
story.append(q("What is Git and why do engineers use it?"))
story.append(a("Git is a version control system that tracks changes to your code over time. Engineers use it so they can collaborate without overwriting each other's work, revert to previous versions if something breaks, and maintain a full history of every change ever made."))
story.append(q("What is the difference between 'git add' and 'git commit'?"))
story.append(a("'git add' stages your changes — it selects what will be included in the next snapshot. 'git commit' takes that staged snapshot and saves it permanently to your local repository history with a message describing what changed."))
story.append(q("What does 'chmod 755' mean in Linux?"))
story.append(a("chmod changes file permissions. 755 means the owner can read, write, and execute (7), while the group and others can only read and execute (5). This is a common permission for executable scripts."))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# MODULE 2: August — Python Intermediate + AWS Cloud Practitioner
# ══════════════════════════════════════════════════════════════════════════════
story.append(module_banner(
    "MODULE 2: Python Intermediate + AWS Cloud Practitioner",
    "August 2026  |  August 1 – August 31  |  ~26 Study Days"
))
story.append(Spacer(1, 10))

story.append(section_box("Overview"))
story.append(Paragraph(
    "This is your most important month. You have two parallel tracks: deepening your Python skills "
    "to intermediate level, and studying for the AWS Cloud Practitioner certification. The cert exam "
    "is your first major milestone and signals to employers that you are serious about cloud. "
    "Study Python mornings, AWS afternoons. Build projects that combine both.",
    body))

story.append(section_box("Daily Schedule  (3–4 hrs)"))
sched2_data = [
    ["TIME", "ACTIVITY"],
    ["8:00–9:30 AM", "Python intermediate lesson (see topics below)"],
    ["9:30–9:45 AM", "Break"],
    ["9:45–11:15 AM", "Python practice project or coding exercise"],
    ["11:15–11:45 AM", "AWS Cloud Practitioner study (Stephane Maarek or Andrew Brown)"],
    ["Evening (optional)", "AWS flashcards, practice questions, GitHub commit"],
]
s2_table = Table(sched2_data, colWidths=[1.8*inch, 4.7*inch])
s2_table.setStyle(TableStyle([
    ("BACKGROUND",  (0,0), (-1,0), TEAL),
    ("TEXTCOLOR",   (0,0), (-1,0), WHITE),
    ("FONTNAME",    (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",    (0,0), (-1,-1), 9),
    ("FONTNAME",    (0,1), (-1,-1), "Helvetica"),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[LIGHT, WHITE]),
    ("GRID",        (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
    ("TOPPADDING",  (0,0), (-1,-1), 4),
    ("BOTTOMPADDING",(0,0),(-1,-1), 4),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
]))
story.append(s2_table)
story.append(Spacer(1, 6))

story.append(section_box("Python Topics to Cover"))
for t in [
    "File I/O — open(), read(), write(), with statement",
    "Exception handling — try/except/finally, custom exceptions",
    "Working with JSON — json.loads(), json.dumps(), reading JSON files",
    "List comprehensions, dictionary comprehensions",
    "Modules and imports — os, sys, math, random, datetime",
    "APIs — using the requests library, parsing JSON responses",
    "Object-Oriented Programming basics — classes, __init__, methods, self",
]:
    story.append(bullet(t))
story.append(Spacer(1, 4))

story.append(section_box("AWS Cloud Practitioner Topics"))
for t in [
    "Cloud concepts: IaaS vs PaaS vs SaaS, shared responsibility model, cloud benefits",
    "IAM: users, groups, roles, policies, MFA, least privilege principle",
    "EC2: instance types, AMIs, security groups, key pairs, pricing models",
    "S3: buckets, objects, storage classes, versioning, static website hosting",
    "VPC: subnets, route tables, internet gateways, NAT gateways",
    "RDS: managed relational databases, Multi-AZ, read replicas",
    "Lambda: serverless compute, triggers, event-driven architecture",
    "CloudWatch: metrics, alarms, logs, dashboards",
    "Billing: Cost Explorer, Budgets, Free Tier, pricing calculator",
    "Global infrastructure: regions, availability zones, edge locations",
]:
    story.append(bullet(t))
story.append(Spacer(1, 6))

story.append(section_box("Projects + Deadlines"))
story.append(project_table([
    ["3", "Expense Tracker", "Aug 10", "Python CLI app that saves expenses to a JSON file; calculates totals by category"],
    ["4", "Contact Book", "Aug 17", "Python CLI CRUD app stored in JSON; add, search, update, delete contacts"],
    ["5", "Weather API App", "Aug 24", "Calls OpenWeatherMap API; displays forecast for any city; handles errors gracefully"],
    ["6", "S3 Static Website", "Aug 28", "Host a simple HTML/CSS site on S3 with public access and static website hosting enabled"],
    ["7", "EC2 Web Server", "Aug 31", "Launch EC2 instance, install nginx/apache, host a webpage, configure security group"],
]))
story.append(deadline("AWS Cloud Practitioner exam: TARGET August 31"))
story.append(Spacer(1, 6))

story.append(section_box("What You Should Know by the End of Module 2"))
for o in [
    "Read/write files and parse JSON data in Python without referencing documentation",
    "Write a Python script that calls a REST API and handles errors",
    "Explain the AWS shared responsibility model and the six pillars of the Well-Architected Framework",
    "Describe what IAM, EC2, S3, VPC, RDS, Lambda, and CloudWatch do — and when to use each",
    "Pass the AWS Cloud Practitioner exam (CLF-C02)",
    "Have 5 projects on GitHub, each with a professional README",
]:
    story.append(outcome(o))
story.append(Spacer(1, 8))

story.append(section_box("Mock Interview — Module 2"))
story.append(q("Explain the AWS shared responsibility model."))
story.append(a("AWS is responsible for the security OF the cloud — the physical hardware, data centers, networking, and hypervisor. Customers are responsible for security IN the cloud — their data, operating systems, network configurations, IAM policies, and application code."))
story.append(q("What is IAM and why is the principle of least privilege important?"))
story.append(a("IAM (Identity and Access Management) controls who can access AWS resources and what they can do. Least privilege means granting only the permissions someone needs to do their job and nothing more. This limits the blast radius if credentials are ever compromised."))
story.append(q("What is the difference between S3 Standard and S3 Glacier?"))
story.append(a("S3 Standard is for frequently accessed data — it has low latency and high throughput. S3 Glacier is for archival storage — it is much cheaper but retrieval takes minutes to hours. You choose based on how often you need the data and your cost constraints."))
story.append(q("What is a VPC and why would you use one?"))
story.append(a("A Virtual Private Cloud is a logically isolated section of AWS where you can define your own network, subnets, route tables, and security rules. You use one to control what resources can talk to each other and what is exposed to the internet."))
story.append(q("Why would you use Lambda instead of EC2?"))
story.append(a("Lambda is serverless — you only pay for the milliseconds your code runs and AWS manages all the infrastructure. EC2 is a virtual machine you provision and manage yourself. Lambda is ideal for event-driven workloads, short-lived tasks, and APIs where you don't want to manage servers."))
story.append(q("How do you handle an exception in Python? Give an example."))
story.append(a("You use a try/except block. For example: 'try: result = 10 / 0' and 'except ZeroDivisionError: print(\"Cannot divide by zero\")'. You can also add 'finally' to run cleanup code regardless of whether an error occurred."))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# MODULE 3: September — AWS Solutions Architect Associate
# ══════════════════════════════════════════════════════════════════════════════
story.append(module_banner(
    "MODULE 3: AWS Solutions Architect Associate + GlamCloud Start",
    "September 2026  |  September 1 – September 30  |  ~26 Study Days"
))
story.append(Spacer(1, 10))

story.append(section_box("Overview"))
story.append(Paragraph(
    "SAA-C03 is a heavyweight cert. Employers take it seriously because it proves you can design "
    "real cloud architectures. Study deeply — don't memorize, understand. This month you also "
    "kick off GlamCloud AI, your flagship portfolio project. Begin building the repository structure "
    "and document your first Architecture Decision Records (ADRs). Take at least one practice exam every week.",
    body))

story.append(section_box("AWS SAA Topics to Cover"))
for t in [
    "EC2 advanced: placement groups, hibernate, instance metadata, user data scripts",
    "VPC deep dive: public/private subnets, NAT Gateway, VPC peering, VPC endpoints, Flow Logs",
    "S3 advanced: lifecycle policies, cross-region replication, presigned URLs, S3 Select",
    "Route 53: routing policies — simple, weighted, latency, failover, geolocation, geoproximity",
    "Load Balancers: ALB vs NLB, target groups, sticky sessions, SSL/TLS termination",
    "Auto Scaling: launch templates, scaling policies, cooldown, health checks",
    "RDS: Multi-AZ vs read replicas, encryption, automated backups, parameter groups",
    "DynamoDB: partition key, sort key, GSIs, LSIs, capacity modes, DAX",
    "Lambda: concurrency, layers, environment variables, VPC integration, destinations",
    "CloudFront: distributions, origins, caching behaviors, signed URLs, OAI/OAC",
    "IAM advanced: roles for services, resource-based policies, SCP, permission boundaries",
    "SQS, SNS: decoupled architecture, fan-out pattern, FIFO queues",
    "ECS, ECR, Fargate: container orchestration basics",
    "CloudFormation: stacks, templates, drift detection",
]:
    story.append(bullet(t))
story.append(Spacer(1, 6))

story.append(section_box("Projects + Deadlines"))
story.append(project_table([
    ["8", "Serverless Image Uploader", "Sep 12", "API Gateway + Lambda + S3. User uploads image via API; Lambda stores it in S3; returns URL"],
    ["9", "Cloud Resume Challenge", "Sep 21", "S3 + CloudFront + Route 53 + DynamoDB + Lambda + API Gateway + GitHub Actions"],
    ["GlamCloud AI", "Begin GlamCloud", "Sep 30", "Create repo with professional structure: ADRs, architecture diagrams, docs folder, README"],
]))
story.append(deadline("AWS Solutions Architect Associate exam: TARGET September 30, 2026"))
story.append(deadline("AWS SAA weekly practice exams every Saturday | Begin GlamCloud repo by Sep 30"))
story.append(Spacer(1, 6))

story.append(section_box("What You Should Know by the End of Module 3"))
for o in [
    "Design a highly available, fault-tolerant architecture on AWS (multi-AZ, load balancing, auto scaling)",
    "Choose the right database service for a given scenario (RDS vs DynamoDB vs ElastiCache)",
    "Explain CloudFront's role in performance and how it integrates with S3",
    "Describe how Route 53 routing policies work and when to use each",
    "Build a serverless API using Lambda, API Gateway, and S3",
    "Have GlamCloud AI repo initialized with professional documentation structure on GitHub",
]:
    story.append(outcome(o))
story.append(Spacer(1, 8))

story.append(section_box("Mock Interview — Module 3"))
story.append(q("What is the difference between an ALB and an NLB?"))
story.append(a("An Application Load Balancer (ALB) operates at Layer 7 (HTTP/HTTPS) and can route based on URL path, hostname, or headers. A Network Load Balancer (NLB) operates at Layer 4 (TCP/UDP) and is designed for ultra-low latency and millions of requests per second. Use ALB for web apps; NLB for gaming, IoT, or real-time streaming."))
story.append(q("What is the difference between Multi-AZ and a read replica in RDS?"))
story.append(a("Multi-AZ creates a synchronous standby in a different AZ for high availability and automatic failover — it is not for scaling reads. A read replica is an asynchronous copy used to scale read traffic. Multi-AZ is for disaster recovery; read replicas are for performance."))
story.append(q("Explain the Cloud Resume Challenge and what services it uses."))
story.append(a("It is a project where you host your resume as a website on S3 with CloudFront for HTTPS delivery, a visitor counter stored in DynamoDB, a Lambda function that updates the counter via API Gateway, and a GitHub Actions pipeline for automated deployment. It demonstrates end-to-end cloud architecture skills."))
story.append(q("What is an Architecture Decision Record (ADR)?"))
story.append(a("An ADR documents why a specific technical decision was made — the context, the options considered, the decision taken, and the consequences. They help teams understand past decisions and avoid repeating the same discussions. They are a sign of engineering maturity."))
story.append(q("When would you use SQS vs SNS?"))
story.append(a("SQS is a message queue where one consumer processes each message — useful for task queues and decoupling services. SNS is a pub/sub system that fans messages out to multiple subscribers simultaneously. A common pattern is to combine them: SNS sends a notification, which triggers multiple SQS queues for different consumers."))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# MODULE 4: October — Terraform + Git/GitHub + Internship Prep
# ══════════════════════════════════════════════════════════════════════════════
story.append(module_banner(
    "MODULE 4: Terraform + Git/GitHub + Internship Preparation",
    "October 2026  |  October 1 – October 31  |  ~26 Study Days"
))
story.append(Spacer(1, 10))

story.append(section_box("Overview"))
story.append(Paragraph(
    "Infrastructure as Code separates junior engineers from everyone else. This month you will stop "
    "clicking in the AWS console and start writing code to provision infrastructure. You will also "
    "go deep on professional Git workflows — branching strategies, pull requests, commit conventions. "
    "Your resume and LinkedIn go live this month, and you start applying to internships.",
    body))

story.append(section_box("Terraform Topics to Cover"))
for t in [
    "HCL syntax: providers, resources, variables, outputs, locals, data sources",
    "State: terraform.tfstate, remote state with S3 + DynamoDB locking",
    "Commands: init, plan, apply, destroy, fmt, validate, import, state",
    "Modules: creating reusable modules, calling modules from root config",
    "Workspaces: managing multiple environments (dev, staging, prod)",
    "Meta-arguments: count, for_each, depends_on, lifecycle",
    "AWS provider: provisioning EC2, VPC, S3, IAM roles, security groups",
]:
    story.append(bullet(t))
story.append(Spacer(1, 4))

story.append(section_box("Git/GitHub Advanced Topics"))
for t in [
    "Branching strategies: Git Flow, trunk-based development, feature branches",
    "Pull requests: writing good PR descriptions, code review etiquette",
    "Conventional commits: feat:, fix:, docs:, chore:, breaking changes",
    "GitHub: branch protection rules, required reviewers, status checks",
    ".gitignore: what to ignore (secrets, .tfstate files, venv, __pycache__)",
    "Git rebase vs merge: when to use each",
]:
    story.append(bullet(t))
story.append(Spacer(1, 6))

story.append(section_box("Projects + Deadlines"))
story.append(project_table([
    ["10", "Terraform Infrastructure", "Oct 14", "Provision EC2 + VPC + security groups + S3 bucket using Terraform; push to GitHub with docs"],
    ["11", "VPC Project", "Oct 24", "Build a full VPC with public/private subnets, NAT gateway, bastion host using Terraform modules"],
    ["Resume + LinkedIn", "Career Docs", "Oct 31", "Professional resume listing projects, certifications, and skills; LinkedIn profile with GitHub link"],
]))
story.append(deadline("Resume live and internship applications begin: October 31"))
story.append(Spacer(1, 6))

story.append(section_box("What You Should Know by the End of Module 4"))
for o in [
    "Write Terraform code to provision any basic AWS infrastructure from scratch",
    "Explain what terraform plan does and why you always run it before apply",
    "Manage Terraform state safely using remote backend (S3 + DynamoDB)",
    "Create and use a reusable Terraform module",
    "Follow professional Git workflow: feature branch → pull request → merge",
    "Have a polished resume and LinkedIn profile ready for employers",
]:
    story.append(outcome(o))
story.append(Spacer(1, 8))

story.append(section_box("Mock Interview — Module 4"))
story.append(q("What is Infrastructure as Code and why does it matter?"))
story.append(a("IaC means managing and provisioning infrastructure through code files rather than manual processes. It matters because it makes infrastructure reproducible, version-controlled, and auditable. You can spin up identical environments in minutes, catch configuration drift, and collaborate with teammates using the same Git workflows you use for application code."))
story.append(q("What does 'terraform plan' do?"))
story.append(a("It shows you exactly what Terraform will create, modify, or destroy before it makes any changes. It is a dry run that compares your configuration against the current state file. You should always review the plan output before running 'terraform apply' — especially in production."))
story.append(q("What is Terraform state and why is it important to store it remotely?"))
story.append(a("The state file (terraform.tfstate) is Terraform's record of what infrastructure it manages. It maps your HCL config to real cloud resources. You store it remotely (S3 + DynamoDB) so your team can collaborate without state conflicts, so it is backed up, and so state locking prevents two people from running apply at the same time."))
story.append(q("What is the difference between 'count' and 'for_each' in Terraform?"))
story.append(a("'count' creates N identical resources using a number. 'for_each' iterates over a map or set, creating one resource per element with a unique key. for_each is generally preferred because removing an element from the middle of a count list causes Terraform to re-number everything, potentially destroying and recreating resources."))
story.append(q("Walk me through a project on your GitHub. What problem does it solve?"))
story.append(a("Pick your strongest project. Structure your answer: 'I built X to solve Y problem. I used [technologies]. The architecture is [brief description]. The hardest challenge was [honest answer]. Here is what I would do differently: [shows growth mindset].'"))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# MODULE 5: November — Docker + Linux + CI/CD + Portfolio Polish
# ══════════════════════════════════════════════════════════════════════════════
story.append(module_banner(
    "MODULE 5: Docker + Linux + CI/CD + Portfolio Polish",
    "November 2026  |  November 1 – November 30  |  ~25 Study Days"
))
story.append(Spacer(1, 10))

story.append(section_box("Overview"))
story.append(Paragraph(
    "Containerization is now a baseline skill for cloud engineers. This month you will learn Docker "
    "deeply, set up automated CI/CD with GitHub Actions, and continue daily Linux practice. "
    "You will also be applying to 10+ internships per week — the portfolio you built is your proof of work. "
    "Practice interview questions twice a week on Saturdays and Wednesdays.",
    body))

story.append(section_box("Docker Topics to Cover"))
for t in [
    "Images vs containers: layers, base images, image registry (Docker Hub, ECR)",
    "Dockerfile: FROM, RUN, COPY, WORKDIR, EXPOSE, CMD, ENTRYPOINT, ENV, ARG",
    "Commands: docker build, run, ps, stop, rm, exec, logs, inspect, pull, push",
    "Volumes: bind mounts vs named volumes; persisting data",
    "Networking: bridge, host, none, container-to-container communication",
    "Docker Compose: multi-container apps, services, depends_on, environment files",
    "Best practices: .dockerignore, multi-stage builds, non-root users, minimal images",
]:
    story.append(bullet(t))
story.append(Spacer(1, 4))

story.append(section_box("GitHub Actions / CI/CD Topics"))
for t in [
    "Workflow syntax: .github/workflows/*.yml, on triggers, jobs, steps, uses",
    "Actions marketplace: actions/checkout, actions/setup-python, aws-actions",
    "Secrets: storing AWS credentials, environment variables in GitHub Settings",
    "CI pipeline: lint → test → build → push to ECR",
    "CD pipeline: deploy to EC2 or Lambda on merge to main",
    "Status badges and branch protection rules tied to workflow status",
]:
    story.append(bullet(t))
story.append(Spacer(1, 6))

story.append(section_box("Projects + Deadlines"))
story.append(project_table([
    ["11", "Dockerized FastAPI App", "Nov 14", "FastAPI REST API containerized with Docker; pushed to Docker Hub or ECR; documented"],
    ["12", "Monitoring Dashboard", "Nov 21", "CloudWatch dashboard + Lambda alarm + SNS notification for a service you built earlier"],
    ["14", "CI/CD Pipeline", "Nov 30", "GitHub Actions pipeline that lints, tests, builds Docker image, and deploys to AWS on push to main"],
]))
story.append(deadline("Apply to 10+ internships/jobs every week throughout November"))
story.append(Spacer(1, 6))

story.append(section_box("What You Should Know by the End of Module 5"))
for o in [
    "Write a Dockerfile from scratch and explain every instruction",
    "Run a multi-container application using Docker Compose",
    "Explain what a CI/CD pipeline is and build one with GitHub Actions",
    "Push a Docker image to ECR and describe the workflow",
    "Use Linux commands fluently: grep, awk, sed, ps, top, netstat, curl, ssh",
    "Be actively applying to internships with a strong portfolio behind every application",
]:
    story.append(outcome(o))
story.append(Spacer(1, 8))

story.append(section_box("Mock Interview — Module 5"))
story.append(q("What is the difference between a Docker image and a Docker container?"))
story.append(a("An image is a read-only blueprint — like a class in programming. A container is a running instance of that image — like an object. You can run multiple containers from the same image, each isolated from one another."))
story.append(q("What is a multi-stage Docker build and why would you use it?"))
story.append(a("A multi-stage build uses multiple FROM statements in a single Dockerfile. You build your application in a heavy base image (with compilers and dev tools), then copy only the compiled output into a minimal runtime image. The final image is much smaller and has a smaller attack surface."))
story.append(q("Explain what CI/CD means and why companies use it."))
story.append(a("CI (Continuous Integration) means developers merge code frequently and automated tests run on every commit to catch bugs early. CD (Continuous Delivery/Deployment) means that passing code is automatically deployed to staging or production. Together they reduce the time between writing code and getting it in front of users, and they reduce human error from manual deployments."))
story.append(q("How do you store secrets in a GitHub Actions workflow?"))
story.append(a("You store them as encrypted secrets in the repository or organization settings under Settings > Secrets. In the workflow file you reference them as ${{ secrets.MY_SECRET }}. Never hardcode credentials in your workflow files or commit them to your repo."))
story.append(q("Tell me about a time you debugged a problem. What was your process?"))
story.append(a("Use the STAR method: Situation (what were you building), Task (what went wrong), Action (how you debugged — logs, isolation, documentation), Result (what you fixed and what you learned). Be specific and honest."))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# MODULE 6: December — Kubernetes + Security + GlamCloud MVP + Job Search
# ══════════════════════════════════════════════════════════════════════════════
story.append(module_banner(
    "MODULE 6: Kubernetes + Security + GlamCloud MVP + Job Search",
    "December 2026  |  December 1 – December 31  |  Final Sprint"
))
story.append(Spacer(1, 10))

story.append(section_box("Overview"))
story.append(Paragraph(
    "This is your culmination month. You will learn Kubernetes fundamentals, complete your GlamCloud AI MVP, "
    "finish the CI/CD pipeline, and aggressively pursue interviews. By December 31 you should have "
    "10+ GitHub projects, AWS Cloud Practitioner certified, a polished resume and LinkedIn, and active "
    "applications to internships and junior cloud roles. Keep applying 10–15 positions per week and practice "
    "interviews every weekend.",
    body))

story.append(section_box("Kubernetes Topics to Cover"))
for t in [
    "Architecture: control plane (API server, etcd, scheduler, controller manager) vs worker nodes",
    "Core objects: Pods, ReplicaSets, Deployments, Services, Namespaces",
    "Networking: ClusterIP vs NodePort vs LoadBalancer, Ingress controllers",
    "Configuration: ConfigMaps, Secrets, environment variables in pods",
    "Storage: PersistentVolumes, PersistentVolumeClaims, StorageClasses",
    "Health checks: liveness probes, readiness probes, startup probes",
    "kubectl: get, describe, apply, delete, logs, exec, port-forward, rollout",
    "EKS: managed Kubernetes on AWS, node groups, IAM roles for service accounts",
]:
    story.append(bullet(t))
story.append(Spacer(1, 4))

story.append(section_box("Cloud Security Topics"))
for t in [
    "IAM best practices: no root access, MFA on all accounts, role-based access",
    "Encryption: at rest (KMS, S3 SSE) vs in transit (TLS/SSL, ACM)",
    "Secrets management: AWS Secrets Manager vs Parameter Store",
    "Security groups vs NACLs: stateful vs stateless, evaluation order",
    "AWS Shield, WAF, GuardDuty, Security Hub: what each protects against",
    "Vulnerability scanning: ECR image scanning, Trivy for container images",
]:
    story.append(bullet(t))
story.append(Spacer(1, 6))

story.append(section_box("Projects + Deadlines"))
story.append(project_table([
    ["13", "Kubernetes Deployment", "Dec 14", "Deploy Dockerized app to EKS or Minikube; write Deployment + Service + Ingress manifests; add health checks"],
    ["15", "GlamCloud AI MVP", "Dec 28", "Complete flagship project: full architecture, Terraform IaC, CI/CD, ADRs, deployment guide, security docs"],
    ["Portfolio", "Full Portfolio Review", "Dec 31", "All 15 projects on GitHub with READMEs; portfolio site live; resume polished; LinkedIn updated"],
]))
story.append(deadline("GlamCloud AI MVP complete by December 28  |  Portfolio complete by December 31"))
story.append(Spacer(1, 6))

story.append(section_box("What You Should Know by the End of Module 6 (End of Bootcamp)"))
for o in [
    "Deploy and manage containerized applications on Kubernetes",
    "Write Kubernetes manifests (Deployment, Service, ConfigMap, Secret, Ingress)",
    "Explain the AWS shared responsibility model as it applies to security",
    "Describe how to secure secrets in both application code and Kubernetes",
    "Present GlamCloud AI confidently in 2–3 minutes, explaining architecture decisions",
    "Answer technical interview questions across Python, AWS, Terraform, Docker, and Kubernetes",
    "Be AWS Cloud Practitioner certified with SAA in strong progress",
    "Have an active, professional GitHub with 15 projects and consistent commit history",
]:
    story.append(outcome(o))
story.append(Spacer(1, 8))

story.append(section_box("Mock Interview — Module 6 (Full Technical Interview Simulation)"))
story.append(q("Walk me through your GlamCloud AI project — what does it do and how is it architected?"))
story.append(a("'GlamCloud AI is my flagship portfolio project — an AI-powered platform for the beauty industry hosted on AWS. The backend is built with [Python/FastAPI], containerized with Docker, deployed using Kubernetes on EKS. Infrastructure is provisioned with Terraform, deployments are automated via GitHub Actions CI/CD. I documented all major decisions in Architecture Decision Records and the project includes a full security review.' Tailor this to your actual build."))
story.append(q("What is the difference between a Deployment and a ReplicaSet in Kubernetes?"))
story.append(a("A ReplicaSet ensures a specified number of pod replicas are running at any time. A Deployment is a higher-level abstraction that manages ReplicaSets and provides rolling updates, rollback capabilities, and declarative updates. In practice you almost always use Deployments, not ReplicaSets directly."))
story.append(q("What is the difference between a ConfigMap and a Secret in Kubernetes?"))
story.append(a("Both store configuration data, but Secrets are for sensitive data (passwords, tokens, keys) and are base64-encoded and can be encrypted at rest in etcd. ConfigMaps are for non-sensitive configuration like environment settings. Neither should store credentials in a production system without additional encryption — use AWS Secrets Manager instead."))
story.append(q("Why is least privilege important and how do you enforce it on AWS?"))
story.append(a("Least privilege limits the damage if a credential is compromised — the attacker can only do what that credential was allowed to do. On AWS you enforce it with IAM: write narrow policies granting only specific actions on specific resources, use roles instead of long-lived access keys, enable MFA, and regularly audit with IAM Access Analyzer and Trusted Advisor."))
story.append(q("Why do you want to work in cloud engineering?"))
story.append(a("Be authentic. Something like: 'I love that cloud engineering sits at the intersection of software, infrastructure, and scale. I spent this year building [specific projects], getting AWS certified, and learning how production systems actually work. Cloud is where I want to build my career and I am ready to contribute from day one.'"))
story.append(q("Where do you see yourself in two years?"))
story.append(a("'I want to be a confident cloud or DevOps engineer who designs and maintains real production systems. My short-term goal is to land this internship, absorb everything I can, and earn my AWS Solutions Architect certification. Within two years I want to be working on infrastructure that serves real users at scale.'"))
story.append(PageBreak())

# ══════════════════════════════════════════════════════════════════════════════
# FINAL PAGE — KEY RULES & END-OF-YEAR CHECKLIST
# ══════════════════════════════════════════════════════════════════════════════
story.append(module_banner(
    "Academy Rules + End-of-Year Checklist",
    "Keep this page visible. Return to it every Sunday."
))
story.append(Spacer(1, 10))

story.append(section_box("Daily Non-Negotiables"))
for r in [
    "Study Mon–Sat. Sunday = rest + review + GitHub organization.",
    "Push at least one commit to GitHub every study day.",
    "Complete every lab before moving to the next topic.",
    "Write a README for every project before moving on.",
    "Spend 30 minutes on AWS flashcards or practice questions (Aug–Sep).",
    "Log one engineering journal entry per week.",
]:
    story.append(bullet(r))
story.append(Spacer(1, 8))

story.append(section_box("End-of-Year Achievement Checklist"))
checklist = [
    ["STATUS", "ACHIEVEMENT"],
    ["[ ]", "AWS Cloud Practitioner certified (target: Aug 31)"],
    ["[ ]", "AWS Solutions Architect Associate — in progress or complete"],
    ["[ ]", "Python: can write intermediate scripts, APIs, and OOP code"],
    ["[ ]", "Terraform: can provision AWS infrastructure from code"],
    ["[ ]", "Docker: can containerize any application and push to a registry"],
    ["[ ]", "Kubernetes: can deploy and manage pods, services, and deployments"],
    ["[ ]", "15 GitHub projects complete, each with a README"],
    ["[ ]", "GlamCloud AI MVP deployed and documented"],
    ["[ ]", "Professional resume — updated monthly since October"],
    ["[ ]", "LinkedIn profile live with projects and certifications"],
    ["[ ]", "Applying to 10–15 internships/jobs weekly since November"],
    ["[ ]", "Mock interview practice every Saturday throughout bootcamp"],
    ["[ ]", "Weekly engineering journal maintained"],
]
c_table = Table(checklist, colWidths=[0.6*inch, 5.9*inch])
c_table.setStyle(TableStyle([
    ("BACKGROUND",  (0,0), (-1,0), NAVY),
    ("TEXTCOLOR",   (0,0), (-1,0), WHITE),
    ("FONTNAME",    (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",    (0,0), (-1,-1), 10),
    ("FONTNAME",    (0,1), (-1,-1), "Helvetica"),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[LIGHT, WHITE]),
    ("ALIGN",       (0,0), (0,-1), "CENTER"),
    ("VALIGN",      (0,0), (-1,-1), "MIDDLE"),
    ("GRID",        (0,0), (-1,-1), 0.5, colors.HexColor("#cccccc")),
    ("TOPPADDING",  (0,0), (-1,-1), 6),
    ("BOTTOMPADDING",(0,0),(-1,-1), 6),
    ("LEFTPADDING", (0,0), (-1,-1), 8),
]))
story.append(c_table)
story.append(Spacer(1, 14))

story.append(Paragraph(
    "You built this. Every commit, every project, every mock interview answer — "
    "it compounds. Stay consistent, stay curious, and keep going.",
    ParagraphStyle("Closing", fontSize=11, textColor=NAVY, fontName="Helvetica-Bold",
                   alignment=TA_CENTER, spaceAfter=4)
))

doc.build(story)
print("PDF generated successfully.")
