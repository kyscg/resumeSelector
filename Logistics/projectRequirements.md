# Software Systems Development: Project Requirements

- [General Details](#general-details)
- [Requirements](#requirements)
  - [Stakeholders](#stakeholders)
  - [Roles and Responsibilities of the Stakeholders](#roles-and-responsibilities-of-the-stakeholders)
  - [Requirements in Detail](#requirements-in-detail)
- [Workflow](#workflow)
- [Technology](#technology)

## General Details

- Team Name			: `mkmkm`
- Project Title		: Resume Selector
- Instructor		: Dr. Charu Sharma
- Mentor			: Radhika Rao
- GitHub Repository	: https://github.com/kyscg/resumeSelector
- Members
    - Mahesh Balaji Dudhanale [2021201010]
    - Maturi Sai Shushma [2021201012]
    - Malla Hemalata [2021201066]
    - Kilaru Yasaswi Sri Chandra Gandhi [2021201080]
    - Kaustuv Dash [2021202019]

## Requirements

### Stakeholders

We have identified three major stakeholders for this project. Developers of the codebase / software, recruiters / employers, and applicants / prospective candidates.

The developers of the software refer to the team building the software. The recruiters are the end users that use the software to find relevant candidates via their resumes. The applicants are users who upload their details and resumes to the database.

### Roles and Responsibilities of the Stakeholders

- Developers
	- Build the software.
	- Write the code.
	- Test the code.
	- Write the documentation.
- Recruiters:
	- Use the software to find relevant candidates.
	- Enter keywords of their choice in a search bar.
- Applicants:
	- Upload their resumes to the database.
	- Add skills and rate their proficiency on a scale of 1 to 5.

### Requirements in Detail

| ID | Requirement | Description | Category |
| --- | --- | --- | --- |
| 1 |Landing Page|Design the landing page|Front-end|
| 2 | Recruiter Page |Design the Recruiter Page|Front-end|
| 3 | Applicant Page |Design the Applicant Page|Front-end|
| 4 |Database Schema |Design the database schema|Database|
| 5 |Backend server |Handle HTTP calls|Backend|

## Workflow

- The website will have three pages, the landing page will be end point of the submitted URL. This landing page will contain information about the site and an option for the users to login.
- Two separate pages will be provided, one each for the recruiters and applicants.
- The applicant page will have options to upload resumes, add skills from our dropdown menu and to rate themselves.
- The recruiter page will have options to search for keywords from a dropdown menu. And a display view for the resumes returned.
- Django will handle the integration of the website front end to the database
- A database schema will be designed to store the details of the recruiters and the applicants with unique ids.

## Technology

| Front End | Back End | Database |
| --- | --- | --- |
| HTML | Django | SQL |
| CSS | Python | |
| JavaScript | | |
| Bootstrap | | |

---
