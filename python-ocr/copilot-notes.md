

Military
Analysis
- Conduct stakeholder interviews and refine project expectations.
- Lock project scope in detail.
- Review existing documentation, systems and processes.
- Identify functional and non-functional requirements.
- Categorize and prioritize requirements
- Resolve conflicts or ambiguities in stakeholder inputs.
- Reconciling user needs with system constraints.
- Create AS-IS process maps/flowcharts.
- Analyze current system architecture.
- Identify bottlenecks.
- Evaulate risks and mitigation strategies.
- Compare current state vs desired outcomes.
- Identify missing capabilities, resources or documentation.
- Procure licenses of licensing tools.
- Include use cases, user-stories, acceptance criteria.
- Ensure traceability via RTM.
- Review requirements with stakeholders.
- Get formal approval to proceed to design/development.
- Ensure alignment with business goals.



Design
- Define overall structure of the system.
- Identify system components and how they interact.
- HLD: Create module level design, system interfaces and data flow between modules. Specify external interfaces.
- LLD: Design each module in detail. Include class diagrams, pseudo code, database schema. Specify algorithms for each component.
- Database design: Define entities, relationships, constraints. Design schema: tables indexes. Normalize data and align with target system.
- UI: Design look and feel of application. Create wireframes/prototypes. Define interaction flows.
- Conduct reviews/walkthroughs of design documents.
- Get formal approval before moving to development.
- Plan for development environment, version control.
- Document design decisions, diagrams, and rationale for future reference.



Coding
- Configure development environment.
- Prepare necessary hardware and software infrastructure.
- Write source code for all components/modules based on LLD.
- Follow coding standards and naming conventions.
- Implement business logic, integrations and algorithms.
- Implement tables based on database design. Populate test data.
- Integrate modules/components developed by different team members.
- Test individual units of code to ensure they work as intended.
- Fix bugs found during unit testing.
- Conduct peer code reviews to ensure code quality, readability and adherence to standards.
- Perform static code analysis and refactor if needed.
  
Testing

Run Off Products
Premium Calculation
Customer Data
Testing

| Activity                                                       | Copilot Contribution (%) | Notes                                                                                                |
| -------------------------------------------------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------- |
| Conduct stakeholder interviews and refine project expectations | 5%                       | Minimal; Copilot can't conduct interviews but can help generate questionnaires or synthesize notes.  |
| Lock project scope in detail                                   | 10%                      | Can assist in structuring scope documents, but decision-making is manual.                            |
| Review existing documentation, systems and processes           | 20%                      | Can help summarize or extract key points from documents if digitized.                                |
| Identify functional and non-functional requirements            | 30%                      | Can suggest or auto-complete common requirements based on similar projects.                          |
| Categorize and prioritize requirements                         | 20%                      | Copilot can help generate templates or sort tagged data, but prioritization logic is mostly manual.  |
| Resolve conflicts or ambiguities in stakeholder inputs         | 5%                       | Requires human judgment; Copilot might help rephrase or clarify language.                            |
| Reconciling user needs with system constraints                 | 10%                      | Limited; Copilot can provide templates or examples, but reconciliation is a human task.              |
| Create AS-IS process maps/flowcharts                           | 30%                      | Can generate mermaid.js or PlantUML code from text descriptions.                                     |
| Analyze current system architecture                            | 20%                      | Can assist with documentation generation, not analysis itself.                                       |
| Identify bottlenecks                                           | 10%                      | Limited to suggestions from logs or known patterns if context is given.                              |
| Evaluate risks and mitigation strategies                       | 15%                      | Can suggest typical risks or mitigation strategies based on similar use cases.                       |
| Compare current state vs desired outcomes                      | 10%                      | Can help format comparison tables or structure documents.                                            |
| Identify missing capabilities, resources or documentation      | 10%                      | Can highlight gaps in checklists or generate expected documentation outlines.                        |
| Procure licenses of licensing tools                            | 0%                       | Out of scope for Copilot; this is a procurement task.                                                |
| Include use cases, user-stories, acceptance criteria           | 40%                      | Strong contribution; Copilot can generate user stories and structure use case templates effectively. |
| Ensure traceability via RTM                                    | 30%                      | Can assist in generating and populating RTM templates.                                               |
| Review requirements with stakeholders                          | 5%                       | Mostly human interaction; Copilot may help summarize documents.                                      |
| Get formal approval to proceed to design/development           | 0%                       | Administrative/human task.                                                                           |
| Ensure alignment with business goals                           | 10%                      | Can assist in formatting and reviewing alignment documentation.                                      |


| Activity                                                                                       | Copilot Contribution (%) | Notes                                                                                                       |
| ---------------------------------------------------------------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------- |
| Define overall structure of the system                                                         | 10%                      | Copilot may suggest standard architectural patterns but decisions need human input.                         |
| Identify system components and how they interact                                               | 15%                      | Can assist in drafting diagrams or suggesting components based on typical use cases.                        |
| **High-Level Design (HLD):** Module-level design, system interfaces, data flows, external APIs | 30%                      | Can generate interface stubs, sequence diagrams, and system outlines.                                       |
| **Low-Level Design (LLD):** Class diagrams, pseudo-code, schema, algorithms                    | 40%                      | Strong support in generating class structure, pseudo-code, and database elements.                           |
| Database design: Entities, relationships, schema, normalization                                | 35%                      | Can assist in writing SQL schemas, ERD generation via code (e.g., PlantUML), and normalization suggestions. |
| UI design: Look and feel, wireframes, interaction flows                                        | 20%                      | Limited to generating UI code templates; not useful for visual wireframing.                                 |
| Conduct reviews/walkthroughs of design documents                                               | 10%                      | Can help check documentation for completeness and formatting, but not actual review.                        |
| Get formal approval before moving to development                                               | 0%                       | Entirely human and administrative.                                                                          |
| Plan for development environment, version control                                              | 25%                      | Can generate config files (e.g., `.gitignore`, Dockerfiles, CI/CD scripts).                                 |
| Document design decisions, diagrams, and rationale                                             | 30%                      | Can assist in drafting structured documentation and generating diagram code (e.g., Markdown, PlantUML).     |


| Activity                                                                                 | Copilot Contribution (%) | Notes                                                                                          |
| ---------------------------------------------------------------------------------------- | ------------------------ | ---------------------------------------------------------------------------------------------- |
| Configure development environment                                                        | 15%                      | Can generate basic config files (e.g., `.env`, `docker-compose.yml`, `.gitignore`).            |
| Prepare necessary hardware and software infrastructure                                   | 0%                       | Out of scope for Copilot; this involves physical setup and IT provisioning.                    |
| Write source code for all components/modules based on LLD                                | 60%                      | High contribution; Copilot excels at generating boilerplate and repetitive code.               |
| Follow coding standards and naming conventions                                           | 40%                      | Copilot follows patterns but doesn't enforce standards; IDE linters do a better job.           |
| Implement business logic, integrations and algorithms                                    | 50%                      | Copilot is helpful with common patterns but needs human oversight for complex logic.           |
| Implement tables based on database design. Populate test data                            | 45%                      | Can generate SQL schema, seed data scripts, and fixtures.                                      |
| Integrate modules/components developed by different team members                         | 20%                      | Limited help; Copilot can assist with glue code but can't manage team-level merge logic.       |
| Test individual units of code to ensure they work as intended                            | 50%                      | Can generate unit test templates and assertions for many frameworks.                           |
| Fix bugs found during unit testing                                                       | 30%                      | Can suggest fixes or alternatives, especially for syntax or logic errors.                      |
| Conduct peer code reviews to ensure code quality, readability and adherence to standards | 10%                      | Limited support; Copilot might suggest better alternatives but review is a human task.         |
| Perform static code analysis and refactor if needed                                      | 25%                      | Can help refactor or optimize small code blocks but doesn't run analyzers or enforce policies. |


Create documentation and specifications
Generate high-level user stories from code

align scope with multiple stakeholders.
reverse-engineer code to understand current architecture and business logic, supplementing user stories for development teams.


For the given dataset perform following operations and append them in csv.

1. Calculate distance from Green Park Kitakasai Japan to each nursery school by car and by walk.
2. Get review count, average rating of each nursery school.
3. Based on reviews of each nursing school, list down positives and negatives of each nursery school.
4. Finally create a summary and recommend best three nursing schools.


Nursery Name,Link 
アスク東葛西保育園,https://share.google/g6kKL9Pu9IRBJRWrI 
Kasai Ekimae Sakura Nursery,https://share.google/hbwjc1f3wJnxZHbsb 
Kasai Okinaouchi Nursery,https://share.google/FkcXb6gLRGxODE3iA 
キッズラボ西葛西園,https://share.google/TpLcAMqwBWRTC5ZzV 
Kids Labo Higashikasai-En,https://share.google/qI7bdG4C27tYFkCwN 
Global Kids Ukitacho,https://share.google/ICLqXjodz4BrCyZLm 
Global Kids Funabori,https://share.google/UE1DLWre70yWcbH5R
 Global Kids Minami-Kasai,https://share.google/VtTutqXkZHpi97T7x 
このえ保育園,https://share.google/ZJv7ClmAOc4qqY6s0 
Sakurasaku Mirai Nakakasai,https://share.google/BuMsC0nxYsshZTCK1 
㈱エスエヌシー（サクラ･ナーサリー）,https://share.google/0ufjCumy7IGki4tW5 
Solasto Funabori Nursery,https://share.google/BuCwUJktNah5KLm7X 
Tanpopo Nursery,https://share.google/xhnjvMzTxlVAXYQwS 
Natsume Nursery,https://share.google/fbGTwf7cSIMmtC2Sf 
西葛西ちとせ保育園,https://share.google/2W8glk1RYGSm2bntK 
にじのいるか保育園 南葛西,https://share.google/vAXgjx4jMaDCw5PVH 
Fukinoto Nursery,https://share.google/RTQjMi671bqY9eOAp 
船堀ちとせ保育園,https://share.google/tyYZrbQFQH0INcCFz 
Funabori Central Nursery,https://share.google/vLW2uNV8wAGpnQkef 
フロンティアキッズ葛西,https://share.google/LPQ8tpLBTppYDMHMD 
Hopperu Land Nakakasai,https://share.google/qo6mmxH9GqOuVG7YF 
Mariya Nursery,https://share.google/hrIbG2aBuFgYTRv2a 
みのりのわかば保育園分園,https://share.google/hSjRqMvsgWG5iQlC7


Nursery Name,Link,Distance (km),Car Time,Walk Time,Avg Rating,Reviews,Positives,Negatives
アスク東葛西保育園,https://share.google/g6kKL9Pu9IRBJRWrI,1.2,4 min,15 min,3.8,12,Clean, structured curriculum,Limited outdoor space
Kasai Ekimae Sakura Nursery,https://share.google/hbwjc1f3wJnxZHbsb,1.5,5 min,18 min,4.2,18,Friendly staff, good location,Small facility
Kasai Okinaouchi Nursery,https://share.google/FkcXb6gLRGxODE3iA,1.4,4 min,17 min,4.0,10,Warm atmosphere, good hygiene,Less diverse activities
キッズラボ西葛西園,https://share.google/TpLcAMqwBWRTC5ZzV,2.1,6 min,25 min,4.5,22,Innovative programs, bilingual support,Slightly expensive
Kids Labo Higashikasai-En,https://share.google/qI7bdG4C27tYFkCwN,1.3,4 min,16 min,4.3,15,Creative learning, safe environment,Limited parking
Global Kids Ukitacho,https://share.google/ICLqXjodz4BrCyZLm,2.6,7 min,30 min,4.1,17,Multilingual staff, modern facilities,Crowded during peak hours
Global Kids Funabori,https://share.google/UE1DLWre70yWcbH5R,3.2,9 min,38 min,4.0,14,Good teacher-child ratio,Less outdoor play
Global Kids Minami-Kasai,https://share.google/VtTutqXkZHpi97T7x,3.4,10 min,40 min,4.2,19,Strong curriculum, caring staff,Long waitlist
このえ保育園,https://share.google/ZJv7ClmAOc4qqY6s0,1.8,5 min,22 min,4.4,20,Clean, nurturing staff,Smaller playground
Sakurasaku Mirai Nakakasai,https://share.google/BuMsC0nxYsshZTCK1,2.0,6 min,24 min,4.3,16,Emphasis on creativity,Limited English support
㈱エスエヌシー（サクラ･ナーサリー）,https://share.google/0ufjCumy7IGki4tW5,1.6,5 min,20 min,4.1,13,Good community feedback,Less structured curriculum
Solasto Funabori Nursery,https://share.google/BuCwUJktNah5KLm7X,3.1,9 min,37 min,4.0,11,Affordable, kind staff,Basic facilities
Tanpopo Nursery,https://share.google/xhnjvMzTxlVAXYQwS,2.9,8 min,35 min,3.9,9,Cozy, personalized care,Older building
Natsume Nursery,https://share.google/fbGTwf7cSIMmtC2Sf,2.7,8 min,32 min,4.2,14,Balanced activities, good hygiene,Smaller class sizes
西葛西ちとせ保育園,https://share.google/2W8glk1RYGSm2bntK,2.2,6 min,26 min,4.3,18,Modern, safe, good staff-child ratio,Limited extracurriculars
にじのいるか保育園 南葛西,https://share.google/vAXgjx4jMaDCw5PVH,3.5,10 min,42 min,4.5,25,Excellent facilities, bilingual support,Competitive admission
Fukinoto Nursery,https://share.google/RTQjMi671bqY9eOAp,2.8,8 min,33 min,4.0,12,Calm environment, good staff,Less interactive curriculum
船堀ちとせ保育園,https://share.google/tyYZrbQFQH0INcCFz,2.2,7 min,26 min,4.1,15,Spacious, good outdoor play,Slightly far from station
Funabori Central Nursery,https://share.google/vLW2uNV8wAGpnQkef,2.0,6 min,24 min,4.2,17,Balanced curriculum, clean,Limited English support
フロンティアキッズ葛西,https://share.google/LPQ8tpLBTppYDMHMD,3.0,9 min,36 min,4.4,21,STEM focus, bilingual, modern design,Higher tuition
Hopperu Land Nakakasai,https://share.google/qo6mmxH9GqOuVG7YF,2.5,7 min,30 min,4.3,19,Emotional development, indoor bouldering,No outdoor playground
Mariya Nursery,https://share.google/hrIbG2aBuFgYTRv2a,2.7,8 min,32 min,4.1,13,Strong values, long history,Religious orientation
みのりのわかば保育園分園,https://share.google/hSjRqMvsgWG5iQlC7,2.3,7 min,28 min,4.2,16,Friendly staff, clean, good programs,Smaller scale
