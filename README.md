# CodeCommit Dataset Collection

This project is a pipeline for collecting, filtering, and processing commit data (messages and diffs) from high-quality Python repositories on GitHub. The goal is to create a dataset suitable for training or evaluating models on code changes and commit messages.

## Project Structure & File Descriptions

### Data Collection Pipeline

1.  **`filter_repos.py`**
    *   **Purpose:** Queries the GitHub API to find popular Python repositories.
    *   **Criteria:** >20,000 stars, language: Python, size < 300,000 KB.
    *   **Output:** Saves the repository URLs to `repo_links.csv`.

2.  **`repo_links.csv`**
    *   **Purpose:** A CSV file containing the raw list of repository URLs fetched from the GitHub API.

3.  **`github_repos.txt`**
    *   **Purpose:** A plain text file containing the list of repository URLs to be cloned. This is the input for the cloning script.

4.  **`clone_project.py`**
    *   **Purpose:** Reads URLs from `github_repos.txt` and clones the repositories locally.
    *   **Output:** Repositories are cloned into the `repos/` directory.

5.  **`repos/`**
    *   **Purpose:** The directory where all the target repositories are cloned.

### Data Extraction & Processing

6.  **`extract_data.py`**
    *   **Purpose:** Iterates through the cloned repositories in `repos/`.
    *   **Functionality:**
        *   Extracts commit messages and their corresponding diffs.
        *   Filters out non-English messages and binary files.
        *   Limits the number of commits per repository (default: 50).
    *   **Output:** Saves the structured data to `repo_commit_data.json`.

7.  **`repo_commit_data.json`**
    *   **Purpose:** The intermediate JSON dataset containing objects with `commit_message` and `diff` fields.

8.  **`extract_clean_data_txt.py`**
    *   **Purpose:** Reads the JSON dataset and formats it into a clean, human-readable text file.
    *   **Output:** Generates `cleaned_dataset.txt`.

9.  **`cleaned_dataset.txt`**
    *   **Purpose:** The final processed dataset. Each entry consists of a `COMMIT_MESSAGE` block and a `DIFF` block, separated by a delimiter.

### Utilities & Model

10. **`test.py`**
    *   **Purpose:** A utility script to count and verify the number of commit messages collected in `repo_commit_data.json`.

## Usage Workflow

1.  Run `filter_repos.py` to get a list of repositories.
2.  Ensure `github_repos.txt` contains the desired URLs.
3.  Run `clone_project.py` to clone the repositories.
4.  Run `extract_data.py` to mine commits and diffs.
5.  Run `extract_clean_data_txt.py` to generate the final text dataset.
