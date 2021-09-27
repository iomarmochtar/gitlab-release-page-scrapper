# Gitlab Release Scrapper

Just a simple script for scrapping some points in Gitlab release page, the script it self created as module in mind so then can be included to other one such as a [bot application](https://github.com/iomarmochtar/cakap).

## Requirements

- `make`
- `python` >= 3.6
- `venv` module

if you are using Ubuntu simply run following commands
```bash
sudo apt install make python3-venv
```

### Install

```bash
make setup
```

## Using the Scripts

make sure to activate virtual env before execute script.
```
source virtenv/bin/activate
```

- `scrap_features.py` is for scrapping list of features in major or minor release page. eg:
```bash
python scrap_features.py -u https://about.gitlab.com/releases/2021/09/22/gitlab-14-3-released/ 
```

- `scrap_table.py` is for scrap list of security release table, it's sorted by severity score from critical to low.
```bash
python scrap_table.py -u https://about.gitlab.com/releases/2021/04/28/security-release-gitlab-13-11-2-released
```

## Development

### Install Dependencies

```bash
make dev
```

### Running Tests

It will do unit test and python typing checks
```bash
make tests
```