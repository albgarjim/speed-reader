# Speed reader

[//]: # "References"
[contact-alberto]: albgarjim1@gmail.com
[reader-gif]: ./docs/reader-gif.gif

Toy speedreader made with python
<!-- description of what the project does  -->

## Table of Contents

- [Project title](#project-title)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Results](#results)
  - [Installation](#installation)
  - [Usage](#usage)
  - [License](#license)
  - [Contact](#contact)

## Introduction

This project is a small speed reader, it can be used with custom text, wikipedia articles and PDF documents

## Results

When the code is launch, the following window will open with the text:
![][reader-gif]

The project incorporates shortcuts to change the speed the text moves, go backwards and pause.
<!-- results of what the project does, add images and gifs -->

## Installation


Clone this repository with the command:

```sh
git clone https://github.com/albgarjim/speed-reader.git
```

Navigate into the src file insidie the `speed-reader` folder:

```sh
cd ./src/speed-reader
```

This project requires the following python libraries:
- enum
- PyPDF2
- wikipedia

They can be installed wiht the command:
```
pip install <library-name>
```

<!-- name technologies used and how to build project -->


## Usage

The reader can be configured on the `configy.py` file. The key points are:
```
format_type = Format.<format>
```
Where `<format>` can be URL, TEXT or PDF depending of the type of text that you want to read.
note: URL corresponds to the url of a wikipedia page
<!-- how to use the project, add code fragments if needed -->


## License

Released under MIT license


## Contact

Maintainer: [Alberto Garcia][contact-alberto]
