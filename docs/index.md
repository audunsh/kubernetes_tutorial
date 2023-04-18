# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Mermaid integration

```mermaid 
graph LR
Data --> Filter_1
Filter_1 -->|Sidechain | Filter_2
Filter_1 --> Rotation
Data --> Filter_2
Filter_2 --> Partition
Rotation --> Partition

subgraph Partition
direction LR
points_1 --> segment_1
points_2-->segment_2
points_1 --> segment_2
points_2 --> segment_1
end
Partition --> Return
```

## Project overview

::: src.server


## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
