# Demo Sales Dashboard

## Usage
- [Usage](#usage)
- [Demo Sales Dashboard](#what-is-demo-sales-dashboard)
- [Directory Structure](#directory-structure)
- [License](#license)
- [Installation](#installation)
- [Contributing](#contributing)
- [Code of conduct](#code-of-conduct)

## Source

The logic and idea, as well as part of the code of this application, come from Sven Bosau. The original code can be found [here](https://github.com/Sven-Bo/streamlit-sales-dashboard). It was recreated using Taipy.

## What is demo Sales Dashboard

Three folders corresponding to three applications can be found in this repository. There are the same 
application at different steps of production. One application is a simple one page dashboard.
The second show how to convert it to a multi-page dashboard where you can integrate data and run scenarios 
with predictions. The last shows how you can leverage Taipy Enterprise to create authentication and 
authorization inside your application.

[Demo Sales Dashboard](https://github.com/Avaiga/demo-sales-dashboard) demonstrates how Taipy can read an Excel or a CSV file and show interesting results. This will the base of our DataViz application. The user can filter it based on city, customer, and gender. This allows users to see metrics specific to certain groups of people or locations. For example, one's can view the data to see sales metrics for customers in a particular city or sales metrics depending on gender.

Many charts are shown on the Web app: sales by hour or sales by product. These graphs can help users identify trends and patterns in the data.

Overall, this demo of Excel/CSV-based app creation allows users to quickly and easily create an app that displays important metrics and charts from their Excel data. The ability to filter it by various criteria makes it easy to gain insights and make informed decisions.


### Demo Type
- **Level**: Medium
- **Topic**: Taipy
- **Components/Controls**: 
  - Taipy GUI: selector, chart, interactive elements, scenario, 

## How to run

This demo works with a Python version superior to 3.8. Install the dependencies of the *requirements.txt* and run the *main.py*.


## Directory Structure


- `src/`: Contains the demo source code of the multi-page version.
- `src_single_page_taipy_tech_talk/`: Contains the demo source code of the single page version.
- `src_enterprise/`: Contains the demo source code of the multi-page version with authentication and authorization.
- `docs/`: contains the images for the documentation
- `CODE_OF_CONDUCT.md`: Code of conduct for members and contributors of _demo-sales-dashboard_.
- `CONTRIBUTING.md`: Instructions to contribute to _demo-sales-dashboard_.
- `INSTALLATION.md`: Instructions to install _demo-sales-dashboard_.
- `LICENSE`: The Apache 2.0 License.
- `Pipfile`: File used by the Pipenv virtual environment to manage project dependencies.
- `README.md`: Current file.

## License
Copyright 2022 Avaiga Private Limited

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at
[http://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

## Installation

Want to install _demo sales dashboard_? Check out our [`INSTALLATION.md`](INSTALLATION.md) file.

## Contributing

Want to help build _demo sales dashboard_? Check out our [`CONTRIBUTING.md`](CONTRIBUTING.md) file.

## Code of conduct

Want to be part of the _demo sales dashboard_ community? Check out our [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) file.
