
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT DESCRIPTION -->
<br />

  <h3 align="center">Django REST API Website for STRATIV</h3>

  <p align="center">
    A django project implementing REST API with customized webpage UI.
    <br />
    <br />
    <a href="https://github.com/AR-Ashraf/Django-REST-API-Website/issues">Report Bug</a>
    ·
    <a href="https://github.com/AR-Ashraf/Django-REST-API-Website/issues">Request Feature</a>
  </p>
  
  
![Screenshot 2021-08-20 023015](https://user-images.githubusercontent.com/65129467/130139781-24c0c805-f52f-434d-bd62-f2cf61f7bc8a.png)



  


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Screenshot 2021-08-20 023050](https://user-images.githubusercontent.com/65129467/130139821-d7818526-c8d0-4a46-962a-4ce98c19b238.png)


Django is a very popular web framework for developing websites and web apps. This project is a task given by the company STRATIV to me for evaluating my Django and Python knowledge.

Through this project:
* You will be able to learn how to design django UI.
* You will learn how to code & run Custom Management Commands in Django.
* You will be able to implement custom made REST API in django projects.
* You will be able to make user authentication & API token authentication.



A list of commonly used resources that I find helpful are listed in the acknowledgements.

## Built With

* [Pycharm](https://www.jetbrains.com/pycharm/)
* [Django Framework](https://www.djangoproject.com/)
* [Django REST Framework](https://www.django-rest-framework.org/)


<!-- GETTING STARTED -->
## Getting Started

To get started with this project to run locally follow the steps below. After that you will be ready to go.

### Prerequisites

Please clone the repo using the following command in your git bash. Or you choose to use the Clone option at the top right corner of this page to copy the link and clone it into your IDE directly.
* Clone the repo
  ```sh
  git clone https://github.com/AR-Ashraf/Django-REST-API-Website.git
  ```
Open the project from your cloned directory in Pycharm. [Make sure you have installed the Django module from setting->python interpreter->add module]

### Installation

1. Install Python 3.9 and Pip3 in your device and then run the following command to install django
   ```sh
   pip install Django
   ```
   ```sh
   pip install djangorestframework   # For implement REST API
   pip install markdown       # Markdown support for the browsable API.
   pip install django-filter  # Filtering support
   ```
2. Now run the following command to install necessary libraries
   ```sh
   pip install requests
   pip install pillow
   ```
  
3. Now go to the project terminal of pycharm and run the following commands
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Now create super user to access the admin dashboard by running following commands
   ```sh
   python manage.py createsuperuser
   ```
   Provide your admin username, email & password. These credentials will be used to access the admin dashboard.
5. Now run your local server to launch the website by running following command
   ```sh
   python manage.py runserver
   ```
   You will see a ip url in the terminal:  http://127.0.0.1:8000/
   Copy this url and paste it in your browser. You will be redirected to a Login page. Please Sign Up as a new user so that you can be authenticated and get into the main dashboard of the project.
   After Registration, enjoy the website!
   
 <!-- API Uses -->
## API

Available API are
   ```sh
   1) List of all countries: http://127.0.0.1:8000/api/country/list
   2) Detail of a specific country: http://127.0.0.1:8000/api/country/list?search=<country_name>
   3) Create a new country: http://127.0.0.1:8000/api/country/create
   4) Update an existing country: http://127.0.0.1:8000/api/country/<country_name>/update
   5) Delete an existing country: http://127.0.0.1:8000/api/country/<country_name>/delete
   6) Searching a country by partial name: http://127.0.0.1:8000/api/country/list?search=<partial_country_name>
   ```
To access these API, run postman in your local machine. There provide your username & password in the form-data section of Body tab. Using these you need to retrieve your access token.
   ```sh
   http://127.0.0.1:8000/api/token/auth/
   ```
Use this url in the GET method of postman and you will get a token in the result field. Then go to the Header tab and chose Authorizatoin as credential and paste your token inside the value field. 
   ```sh
   Token <Your-Token>
   ```
Provide the token in the value field like this way.
Now use those api urls and send requests & enjoy this project.


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/AR-Ashraf/Django-REST-API-Website/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTION -->
## Contribution

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Dev Branch (`git checkout -b dev/Django-REST-API-Website`)
3. Commit your Changes (`git commit -m 'Add some Django API Feature'`)
4. Push to the Branch (`git push origin dev/Django-REST-API-Website`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

LinkedIn - [Ashraful Islam](https://linkedin.com/in/ashraful-islam-78aa7a1a0) - Send me a connection request and let's get to know each other.

My Other Projects: [Projects](https://github.com/AR-Ashraf?tab=repositories)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [YouTube Link that helped me](https://www.youtube.com/watch?v=ZjAMRnCu-84&t=455s)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/AR-Ashraf/Django-REST-API-Website.svg?style=for-the-badge
[contributors-url]: https://github.com/AR-Ashraf/Django-REST-API-Website/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AR-Ashraf/Django-REST-API-Website.svg?style=for-the-badge
[forks-url]: https://github.com/AR-Ashraf/Django-REST-API-Website/network/members
[stars-shield]: https://img.shields.io/github/stars/AR-Ashraf/Django-REST-API-Website.svg?style=for-the-badge
[stars-url]: https://github.com/AR-Ashraf/Django-REST-API-Website/stargazers
[issues-shield]: https://img.shields.io/github/issues/AR-Ashraf/Django-REST-API-Website.svg?style=for-the-badge
[issues-url]: https://github.com/AR-Ashraf/Django-REST-API-Website/issues
[license-shield]: https://img.shields.io/github/license/AR-Ashraf/Django-REST-API-Website.svg?style=for-the-badge
[license-url]: https://github.com/AR-Ashraf/Django-REST-API-Website/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/ashraful-islam-78aa7a1a0

