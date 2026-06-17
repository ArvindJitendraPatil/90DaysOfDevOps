# Day 38 - YAML Basics

## Task 1 - Key Value Pairs

Created person.yaml with:

* name
* role
* experience_years
* learning

![Task 1](images/task1.png)

## Task 2 - Lists

Added:

### Block Style List

```yaml
tools:
  - Docker
  - Kubernetes
  - Jenkins
  - Terraform
  - GitHub Actions
```

### Inline Style List

```yaml
hobbies: [Learning New Technologies, Cricket, Reading, Travelling]
```
![Task 2](images/task2.png) 

## Task 3 - Nested Objects

Created server.yaml with nested:

* server
* database
* credentials

![Task 3.1](images/task3.1.png)  
![Task 3.2](images/task3.2.png)

## Task 4 - Multi-line Strings

Used:

### Pipe Style

```yaml
startup_script_preserve: |
```

Preserves line breaks.

### Fold Style

```yaml
startup_script_fold: >
```

Converts multiple lines into a single line.

![Task 4](images/task4.png)

## Task 5 - YAML Validation

Validated files using:

```bash
yamllint person.yaml
yamllint server.yaml
```

Fixed indentation errors and revalidated successfully.

![Task 5](images/task5.png)

## Task 6 - Spot the Difference

Incorrect indentation caused YAML parsing errors.

Correct YAML requires consistent spacing.

![Task 6.1](images/task6.1.png)  
![Task 6.2](images/task6.2.png)


## What I Learned

1. YAML is indentation-sensitive and uses spaces only.
2. Lists can be written in block style or inline style.
3. The `|` operator preserves new lines while `>` folds lines into a single paragraph.

