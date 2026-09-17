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

Agentic-YouTube-Creator-Copilot/
│
├── app/
│   ├── agents/
│   │   ├── content_analyst.py
│   │   ├── content_writer.py
│   │   ├── seo_analyst.py
│   │   └── validator.py
│   │
│   ├── models/
│   │   └── schemas.py
│   │
│   ├── prompts/
│   │   ├── content_analyst.txt
│   │   ├── content_writer.txt
│   │   ├── seo_analyst.txt
│   │   └── validator.txt
│   │
│   ├── services/
│   │   └── llm.py
│   │
│   ├── tools/
│   │   ├── transcript_cleaner.py
│   │   └── youtube.py
│   │
│   └── workflow/
│       ├── content_node.py
│       ├── decision.py
│       ├── revision_node.py
│       ├── seo_node.py
│       ├── state.py
│       ├── validator_node.py
│       ├── writer_node.py
│       └── youtube_node.py
│
├── main.py
├── requirements.txt
│
├── test_content_analyst.py
├── test_content_node.py
├── test_content_writer.py
├── test_decision.py
├── test_seo_analyst.py
├── test_seo_node.py
├── test_transcript_cleaner.py
├── test_validator.py
├── test_validator_node.py
├── test_workflow_state.py
├── test_writer_node.py
├── test_youtube.py
└── test_youtube_node.py


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


