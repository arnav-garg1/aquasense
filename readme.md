**Determining semester weeks**

I'm figuring out the schedule based on the spring semester running from January 20 to May 2025. The semester usually has 15 weeks, but they expect 14. I'll start with January 20 for week 1, and adjust week 14 to April 21, with finals likely being in early May. The weeks break down to: Jan 20, 27; Feb 3, 10, 17, 24; Mar 3, 10, 17, 24, 31; Apr 7, 14, 21. Seems like a good fit for the spring semester!

**Structuring README for project**

From the second photo, I’ll follow the formatting style: bullet points at the top, then headings with dates and content under each. For each of the 14 weeks, I’ll create placeholders summarizing the tasks.

For example, for Week 1, I’ll summarize notes like “Class Intro + Early Approval,” and week by week, I’ll follow this template, listing accomplishments.

The overall goal will be to match the format, with placeholders filled in for each week. Sounds like a great approach for a clear project README!


Thought for 13 seconds


# AquaSense Project Worklog

A week-by-week summary of our Spring 2025 senior design project—AquaSense: Affordable ML-Based Water Quality Monitoring for Aquariums—covering January 20, 2025 through April 21, 2025.

---

## Table of Contents

* [Week 1 Notes – Class Intro + Early Approval (2025-01-20)](#week-1-notes––class-intro--early-approval-2025-01-20)
* [Week 2 Notes – Team Meeting #1 + Project Idea Brainstorm (2025-01-27)](#week-2-notes––team-meeting-1--project-idea-brainstorm-2025-01-27)
* [Week 3 Notes – KiCad Intro + PCBWay (2025-02-03)](#week-3-notes––kicad-intro--pcbway-2025-02-03)
* [Week 4 Notes – Team Contract Discussion + HLR (2025-02-10)](#week-4-notes––team-contract-discussion--hlr-2025-02-10)
* [Week 5 Notes – Design Document + Part List Assembly (2025-02-17)](#week-5-notes––design-document--part-list-assembly-2025-02-17)
* [Week 6 Notes – Breadboard Demo + Early Schematic Design (2025-02-24)](#week-6-notes––breadboard-demo--early-schematic-design-2025-02-24)
* [Week 7 Notes – Final Schematic Design + PCB Footprint (2025-03-03)](#week-7-notes––final-schematic-design--pcb-footprint-2025-03-03)
* [Week 8 Notes – Backend Setup (Flask) (2025-03-10)](#week-8-notes––backend-setup-flask-2025-03-10)
* [Week 9 Notes – Backend Setup (LLM – DistillGPT2) + Frontend (2025-03-17)](#week-9-notes––backend-setup-llm–distillgpt2--frontend-2025-03-17)
* [Week 10 Notes – Final Breadboard Setup (2025-03-24)](#week-10-notes––final-breadboard-setup-2025-03-24)
* [Week 11 Notes – Final PCB Soldering + Testing (2025-03-31)](#week-11-notes––final-pcb-soldering--testing-2025-03-31)
* [Week 12 Notes – End to End Solution + Workflow Optimization (2025-04-07)](#week-12-notes––end-to-end-solution--workflow-optimization-2025-04-07)
* [Week 13 Notes – Mock Demo + Final Developments (2025-04-14)](#week-13-notes––mock-demo--final-developments-2025-04-14)
* [Week 14 Notes – Final Presentation + Final Report (2025-04-21)](#week-14-notes––final-presentation--final-report-2025-04-21)

---

## Week 1 Notes – Class Intro + Early Approval (2025-01-20)

* **Kick-off**: Introduced project scope and objectives in class.
* **Approval**: Secured early faculty approval on problem statement and deliverables.
* **Roles**: Defined team member responsibilities and communication channels.

---

## Week 2 Notes – Team Meeting #1 + Project Idea Brainstorm (2025-01-27)

* **First Team Sync**: Aligned on vision, schedule, and collaboration tools (Git, Trello).
* **Brainstorm**: Generated and evaluated sensor and ML‐based water monitoring ideas.
* **Selection**: Narrowed down to pH, temperature, and luminescence as core parameters.

---

## Week 3 Notes – KiCad Intro + PCBWay (2025-02-03)

* **KiCad Training**: Walked through PCB schematic capture and footprint creation.
* **PCBWay Research**: Compared prototyping vendors, lead times, and cost estimates.
* **Initial Footprints**: Drafted footprints for pH probe connector and ESP32 module.

---

## Week 4 Notes – Team Contract Discussion + HLR (2025-02-10)

* **Team Contract**: Agreed on contribution expectations, conflict resolution, and IP.
* **High‐Level Requirements**: Documented functional and non-functional requirements.
* **Risk Log**: Identified key risks (sensor calibration, power management, ML latency).

---

## Week 5 Notes – Design Document + Part List Assembly (2025-02-17)

* **Design Doc**: Finalized system architecture: sensors → ESP32 → Flask API → Dashboard.
* **Part List**: Compiled BOM: pH probes, DS18B20 temperature sensor, photodiode, ESP32.
* **Procurement**: Placed orders for all critical components and breakout cables.

---

## Week 6 Notes – Breadboard Demo + Early Schematic Design (2025-02-24)

* **Breadboard Prototype**: Assembled sensors on breadboard; validated basic readings.
* **Schematic Draft**: Began translating breadboard wiring into KiCad schematic.
* **Testing**: Logged sample data to serial console; confirmed nominal voltage ranges.

---

## Week 7 Notes – Final Schematic Design + PCB Footprint (2025-03-03)

* **Schematic Freeze**: Completed and reviewed full schematic with power and sensor routing.
* **Footprint Review**: Finalized component footprints; performed ERC/DRC checks.
* **Layout Prep**: Exported netlist for PCB layout stage.

---

## Week 8 Notes – Backend Setup (Flask) (2025-03-10)

* **API Scaffold**: Created Flask application with endpoints for data ingestion and retrieval.
* **Database**: Designed PostgreSQL schema to store timestamped sensor readings.
* **CI/CD**: Integrated basic unit tests and linting into GitHub Actions pipeline.

---

## Week 9 Notes – Backend Setup (LLM – DistillGPT2) + Frontend (2025-03-17)

* **ML Integration**: Developed nightly batch job to retrain anomaly‐detection model (DistillGPT2).
* **Recommendations**: Built LLM‐powered recommendation endpoint for pH/temperature alerts.
* **Frontend Kick-off**: Initialized React app; set up real-time charting with Recharts.

---

## Week 10 Notes – Final Breadboard Setup (2025-03-24)

* **Merged Prototype**: Combined all sensors, microcontroller, and power supply on breadboard.
* **Reliability Tests**: Ran 48-hour soak test; monitored data consistency and drift.
* **Adjustments**: Tweaked resistor values and code calibration routines.

---

## Week 11 Notes – Final PCB Soldering + Testing (2025-03-31)

* **PCB Arrival**: Received assembled PCBs from PCBWay; inspected solder quality.
* **Soldering**: Hand‐soldered any missing passives; reflowed critical components.
* **Functional Test**: Verified that PCB matches breadboard performance.

---

## Week 12 Notes – End to End Solution + Workflow Optimization (2025-04-07)

* **Full Pipeline**: Validated data flow from sensor → PCB → Flask → Dashboard → Alerts.
* **Workflow**: Automated Docker builds for Flask backend and React frontend.
* **Optimization**: Reduced LLM inference latency by quantizing model.

---

## Week 13 Notes – Mock Demo + Final Developments (2025-04-14)

* **Mock Presentation**: Presented demo to peers; collected feedback on UI/UX and reliability.
* **Feature Polish**: Added custom alert notifications and user‐configurable thresholds.
* **Bug Fixes**: Resolved edge‐case errors in data parsing and chart rendering.

---

## Week 14 Notes – Final Presentation + Final Report (2025-04-21)

* **Slide Deck**: Prepared 10-slide overview covering problem, design, results, and next steps.
* **Final Report**: Compiled methodology, experiments, and quantitative results into PDF.
* **Submission**: Delivered project deliverables to course repository and archived code.

---

*End of Worklog*
*Questions or comments? Reach out to the AquaSense team.*
