# Contributing

## Introduction

ObjectiFai uses a CI/CD pipeline to automate the process of building, testing, and deploying the project. When contributing to ObjectiFai, you should follow the guidelines in this document to ensure that your changes are compatible with the CI/CD pipeline.

## Joining the project as a contributor

If you want to join the project as a contributor, you should first fork the project to your own GitHub account. Then, you should clone the forked repository to your local machine. After that, you should add the original repository as a remote repository to your local repository. Finally, you should create a new branch for your changes. The following commands can be used to do this:

```bash
git clone https://github.com/dwerkjem/ObjectiFai.git # clone the forked repository
cd ObjectiFai # change the working directory to the local repository
git remote add upstream
git checkout -b <branch-name> # create a new branch for your changes
```

## Making changes

When making changes to the project, you should follow the guidelines in this section to ensure that your changes are compatible with the CI/CD pipeline.

### Commit messages

describe your changes in the commit message. The commit message should be in the following format:

```plaintext
<short>

<long>
```

for example:

```plaintext
fix: typo in README.md

fixes a typo in README.md
```

## Reporting issues and requesting features

If you want to report an issue or request a feature, you should create an issue in the issue tracker. When creating an issue, you should follow this template:

isuue title: `<type>: <short description>`
issue body:

```plaintext
## Description

<long description>
```

for example:

issue title: `bug: typo in README.md`
issue body:

```plaintext
## Description

there is a typo in README.md at line 3 in the word "ObjeteFai" it should be "ObjectiFai"
```
