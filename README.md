# AChDA News Pipeline

## What this is
Web content standardization and translation (ES→EN) pipeline. Content must follow the structure defined in `template.xml` to be processed by the script. See **Before you start** before running anything.

## Before you start

All files must follow this naming convention:

| File | Format |
|---|---|
| Article text | `DD-MM-YYYY_titulo-corto.xml` |
| Header image | `DD-MM-YYYY-head.jpg` |
| Body images | `DD-MM-YYYY-body(1).jpg`, `DD-MM-YYYY-body(2).jpg`... |
| Attachment | `DD-MM-YYYY-adjunto.pdf` |

The date is the linking key between text and media files. One news item per date maximum.

XML content must follow the structure in `template.xml`: `<headline>`, `<byline>`, `<dateline>`, `<lead>`, `<body>`, `<tail>`.

The script output follows the same naming format. The translated file will be generated automatically.

## How to run the script

*(To be completed once translate.py is built.)*
