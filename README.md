# Agentic YouTube Creator Copilot

An AI-based project that helps YouTube creators understand their video content and generate useful content from it.

The current version takes a YouTube video, gets its transcript, analyzes the content, generates SEO information, creates a title and description, and then checks the generated content using a validation agent.

If the generated content does not pass validation, the system can revise the content and check it again.

## How It Works

The current workflow is:

YouTube URL
↓
Transcript
↓
Content Analysis
↓
SEO Analysis
↓
Content Generation
↓
Validation
↓
Revision if required

## Main Components

### 1. YouTube Transcript

The system takes a YouTube URL and extracts the video ID.

It then retrieves the available transcript and cleans the text before sending it for analysis.

### 2. Content Analyst

The Content Analyst analyzes the transcript and identifies:

- Main topic
- Subtopics
- Target audience
- Content category
- Content intent
- Key points
- Important facts

### 3. SEO Analyst

The SEO Analyst uses the content analysis to generate:

- Primary keywords
- Secondary keywords
- Long-tail keywords
- Tags
- Hashtags

### 4. Content Writer

The Content Writer generates:

- Title
- Hook
- Description
- Call to action

### 5. Validator

The Validator checks the generated content for:

- Grounding
- Keyword relevance
- Completeness
- Issues
- Suggestions for improvement

### 6. Revision

If the content does not pass validation, the validator's feedback is sent back to the Content Writer.

The Writer generates a revised version, which is checked again.

A maximum revision limit is used to prevent an endless loop.

## Project Structure

## Project Structure

```text
Agentic-YouTube-Creator-Copilot/
│
├── app/
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── content_analyst.py       # Analyzes the video transcript
│   │   ├── content_writer.py        # Generates and revises content
│   │   ├── seo_analyst.py           # Generates SEO keywords, tags and hashtags
│   │   └── validator.py              # Validates the generated content
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py               # Structured data models using Pydantic
│   │
│   ├── prompts/
│   │   ├── content_analyst.txt      # Prompt for Content Analyst
│   │   ├── content_writer.txt       # Prompt for Content Writer
│   │   ├── seo_analyst.txt          # Prompt for SEO Analyst
│   │   └── validator.txt            # Prompt for Validator
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── llm.py                   # Gemini API service
│   │
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── transcript_cleaner.py    # Cleans the extracted transcript
│   │   └── youtube.py               # YouTube URL and transcript handling
│   │
│   └── workflow/
│       ├── __init__.py
│       ├── content_node.py           # Content analysis workflow node
│       ├── decision.py               # Decides whether to finish or revise
│       ├── revision_node.py          # Handles content revision
│       ├── seo_node.py               # SEO analysis workflow node
│       ├── state.py                  # Shared workflow state
│       ├── validator_node.py         # Validation workflow node
│       ├── writer_node.py            # Content generation workflow node
│       └── youtube_node.py           # YouTube processing workflow node
│
├── main.py                           # Runs the complete workflow
├── requirements.txt                  # Project dependencies
├── README.md                          # Project documentation
│
├── test_content_analyst.py           # Tests Content Analyst
├── test_content_node.py              # Tests Content Node
├── test_content_writer.py            # Tests Content Writer
├── test_decision.py                  # Tests workflow decision logic
├── test_seo_analyst.py               # Tests SEO Analyst
├── test_seo_node.py                  # Tests SEO Node
├── test_transcript_cleaner.py        # Tests transcript cleaning
├── test_validator.py                 # Tests Validator
├── test_validator_node.py            # Tests Validator Node
├── test_workflow_state.py            # Tests workflow state
├── test_writer_node.py               # Tests Writer Node
├── test_youtube.py                   # Tests YouTube utilities
└── test_youtube_node.py              # Tests YouTube workflow node


## Technologies Used

* Python
* Gemini API
* Pydantic
* YouTube Transcript API
* python-dotenv
* Git
* GitHub

## Model

The current project uses:    ""Gemini 3.8 Flash""


The model is used for the content analysis, SEO analysis, content generation, validation, and revision tasks.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/ashish1yash/Agentic-YouTube-Creator-Copilot.git


### 2. Create the Conda environment

bash
conda create -n agentic-youtube python=3.13


Activate it:

bash
conda activate agentic-youtube


### 3. Install the dependencies

bash
pip install -r requirements.txt


### 4. Add the Gemini API key

Create a `.env` file in the project folder:

text
GEMINI_API_KEY=your_api_key_here


Do not upload the `.env` file to GitHub.

### 5. Run the project

bash
python main.py


The program will ask for a YouTube URL:

text
Enter YouTube URL:


Enter the URL and the workflow will process the video.

## Example Output

The system generates:

Title:
A Declaration of Romantic Commitment | Love and Loyalty Song Lyrics

Hook:
When feelings have remained unspoken for so long,
what does true devotion look like?

Description:
A description generated from the video's transcript,
content analysis and SEO analysis.

Call to Action:
If this message speaks to you, please like the video
and subscribe for more content.


The generated content is then passed to the Validator.

Example validation result:


Valid: True
Grounding: 1.0
Keyword Relevance: 1.0
Completeness: 1.0
Revisions: 0


## Current Status

The first version of the project is working with a plain Python workflow.

Currently implemented:

* YouTube URL processing
* Transcript extraction
* Transcript cleaning
* Content analysis
* SEO analysis
* Content generation
* Content validation
* Validation-based decision making
* Content revision
* Revision limit

## Future Improvements

Planned improvements include:

* Convert the workflow to LangGraph
* Improve the agent workflow
* Add better evaluation methods
* Add channel-specific information
* Add RAG for creator preferences and previous content
* Add a web interface
* Generate additional content such as Shorts scripts and social media posts
* Improve error handling
* Add monitoring and logging

## Author

**Ashish Kumar**


