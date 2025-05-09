# AquaSense Spring 2025 Project Worklog

A detailed, week-by-week narrative of our senior design journey—AquaSense: an affordable, intelligent aquarium water-quality monitoring system. We started January 20, 2025 and wrapped up April 21, 2025.

---

## Table of Contents

1. [Week 1 (2025-01-20): Class Introduction & Early Approval](#week-1-2025-01-20-class-introduction--early-approval)
2. [Week 2 (2025-01-27): First Team Gathering & Ideation](#week-2-2025-01-27-first-team-gathering--ideation)
3. [Week 3 (2025-02-03): Diving into KiCad & PCBWay Research](#week-3-2025-02-03-diving-into-kicad--pcbway-research)
4. [Week 4 (2025-02-10): Team Charter & High-Level Requirements](#week-4-2025-02-10-team-charter--high-level-requirements)
5. [Week 5 (2025-02-17): System Design Document & BOM Finalization](#week-5-2025-02-17-system-design-document--bom-finalization)
6. [Week 6 (2025-02-24): Breadboard Prototype & Early Schematics](#week-6-2025-02-24-breadboard-prototype--early-schematics)
7. [Week 7 (2025-03-03): Schematic Freeze & Footprint Validation](#week-7-2025-03-03-schematic-freeze--footprint-validation)
8. [Week 8 (2025-03-10): Building the Flask Backend](#week-8-2025-03-10-building-the-flask-backend)
9. [Week 9 (2025-03-17): ML Integration & Frontend Kick-off](#week-9-2025-03-17-ml-integration--frontend-kick-off)
10. [Week 10 (2025-03-24): Final Breadboard Assembly & Stress Tests](#week-10-2025-03-24-final-breadboard-assembly--stress-tests)
11. [Week 11 (2025-03-31): PCB Arrival, Soldering & Validation](#week-11-2025-03-31-pcb-arrival-soldering--validation)
12. [Week 12 (2025-04-07): End-to-End Pipeline & Workflow Refinement](#week-12-2025-04-07-end-to-end-pipeline--workflow-refinement)
13. [Week 13 (2025-04-14): Mock Demo, Feedback & Final Touches](#week-13-2025-04-14-mock-demo-feedback--final-touches)
14. [Week 14 (2025-04-21): Final Presentation & Report Submission](#week-14-2025-04-21-final-presentation--report-submission)

---

## Week 1 (2025-01-20): Class Introduction & Early Approval

* We kicked things off by laying out the big picture: measurable water-quality goals, target user experience, and essential deliverables.
* After presenting our concept in class, we secured faculty buy-in for our project charter—defining scope, timeline, and success criteria.
* Roles were informally assigned: Arnav — technical lead; Anurag — ML pipeline; Michael — UI/UX and testing.

---

## Week 2 (2025-01-27): First Team Gathering & Ideation

* Over coffee, we sketched out over a dozen sensor ideas—everything from dissolved oxygen to conductivity—but landed on pH, temperature, and light as high-impact, low-cost choices.
* Established communication norms: daily stand-ups via Slack, bi-weekly Trello grooming, and weekly GitHub pull-request reviews.
* Mapped out preliminary MVP features: real-time data logging, threshold-based alerts, and basic trend visualization.

---

## Week 3 (2025-02-03): Diving into KiCad & PCBWay Research

* Completed our first hands-on tutorial in KiCad: importing footprints, linking symbols, and running ERC checks.
* Investigated PCB fab houses—PCBWay stood out for its balance of cost, lead time, and support for ENIG finishes.
* Drafted initial footprints for the ESP32 module, DS18B20 sensor, and industry-standard pH probe connector.

---

## Week 4 (2025-02-10): Team Charter & High-Level Requirements

* Finalized our team contract: contribution expectations, conflict resolution protocols, and IP ownership clauses.
* Compiled a High-Level Requirements (HLR) document detailing functional needs (e.g., “system logs one reading per minute”) and non-functional constraints (e.g., “power consumption < 200 mA”).
* Created a risk register: prioritized potential blockers such as sensor calibration drift, Wi-Fi connectivity issues, and model retraining latency.

---

## Week 5 (2025-02-17): System Design Document & BOM Finalization

* Authored the System Design Document, complete with architecture diagrams showing data flow from sensors through the cloud and back to the UI.
* Locked down the Bill of Materials: selected waterproof pH probes, DS18B20 temperature sensors, photodiodes, voltage regulators, and ESP32 DevKitC.
* Placed orders and began tracking shipments for all components; anticipated two-week delivery for custom PCBs from PCBWay.

---

## Week 6 (2025-02-24): Breadboard Prototype & Early Schematics

* Assembled the first breadboard prototype: pH probe, temperature sensor, photodiode, and ESP32 all powered by a bench supply.
* Captured live sensor data in the Arduino Serial Monitor; validated the raw voltage-to-unit conversions against lab-grade meters.
* Began translating the physical wiring into a KiCad schematic—adjusting component labels and net names for clarity.

---

## Week 7 (2025-03-03): Schematic Freeze & Footprint Validation

* After peer review, we “froze” the KiCad schematic—no more topology changes without cross-signoff.
* Conducted footprint sanity checks: measured pad dimensions against datasheet drawings, then performed a quick paper-layout test.
* Generated a netlist and prepared for board layout, ensuring clear separation between high-voltage (probe) and logic domains.

---

## Week 8 (2025-03-10): Building the Flask Backend

* Scaffolded a Flask server with two core endpoints: `POST /readings` for data ingestion and `GET /readings` for dashboard consumption.
* Designed a lightweight PostgreSQL schema—sensor readings table indexed by timestamp and sensor ID for fast queries.
* Enabled continuous integration: automated linting and unit tests run on every Git push via GitHub Actions.

---

## Week 9 (2025-03-17): ML Integration & Frontend Kick-off

* Developed a nightly batch job that retrains our lightweight anomaly-detection model on the past 24 hours of readings—initial proof-of-concept with an XGBoost baseline.
* Wrapped the trained model in a REST endpoint that, given recent trends, returns human-friendly recommendations (e.g., “pH creeping down—consider a 10% water change”).
* Bootstrapped a React frontend: implemented real-time charts with Recharts and styled components with Tailwind CSS.

---

## Week 10 (2025-03-24): Final Breadboard Assembly & Stress Tests

* Consolidated all sensors and electronics onto a single breadboard: confirmed wiring correctness and power-rail stability.
* Ran a 48-hour soak test, logging readings every minute and checking against laboratory reference values; noted ±0.05 pH drift, tuned calibration code.
* Iterated on resistor divider values to maximize ADC resolution without clipping the signal.

---

## Week 11 (2025-03-31): PCB Arrival, Soldering & Validation

* Unboxed PCBs from PCBWay—excellent silkscreen clarity and minimal solder‐mask misalignment.
* Hand‐soldered passives and through-hole connectors; reflowed the ESP32 with our hot-air station.
* Conducted a side-by-side comparison of PCB vs. breadboard readings: results matched within sensor tolerances across all three parameters.

---

## Week 12 (2025-04-07): End-to-End Pipeline & Workflow Refinement

* Verified the complete data flow: sensor → PCB → Flask API → PostgreSQL → React dashboard → alert notifications.
* Containerized the Flask backend and React frontend with Docker, spinning up the full stack locally with a single `docker-compose up`.
* Reduced LLM inference latency by compressing the DistillGPT2 model with 8-bit quantization, cutting response time in half.

---

## Week 13 (2025-04-14): Mock Demo, Feedback & Final Touches

* Delivered a full mock demo to classmates and teaching staff—walked through hardware, software, and ML insights in a 10-minute presentation.
* Incorporated feedback: added user-configurable alert thresholds and an audible buzzer for critical warnings.
* Squashed lingering bugs in CSV export, fixed edge cases in date handling, and polished UI colors for better accessibility.

---

## Week 14 (2025-04-21): Final Presentation & Report Submission

* Finalized our slide deck: concise problem statement, architecture overview, live demo video, and quantitative performance metrics.
* Compiled the comprehensive project report—documenting design rationale, experimental results (drift curves, latency measurements), and future work suggestions.
* Submitted all materials to the course GitHub repository, archived our Docker images, and handed in physical copies of the report.
