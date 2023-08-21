# Mumbai House Price prediction Project

In this end-to-end data science and machine learning project, I Build a model that predict the price of houses in Mumbai. After Hyperparameter tuning and cross validation, I found that a Linear Regression is best for this model. The Model has 87% of accuracy in predicting the house prices.The dataset used is Mumbai prices data set from Kaggle.

![](https://github.com/izam-mohammed/mumbai-home-price/blob/main/UI_website.png?raw=true)

## Get Started

To get started with the Note Taking Website, follow these steps:

1. **Clone the Repository:** Clone this repository to your local machine using the following command:

   ```
   git clone https://github.com/izam-mohammed/Mumbai-Home-Price.git
   cd Mumbai-Home-Price
   ```

2. **Setup Virtualenv (Windows)**:
   ```
   pip install virtualenv
   virtualenv venv
   .\venv\Scripts\Activate
   ```
   **Setup Virtualenv (mac/linux)**:
   ```
   pip install virtualenv
   virtualenv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:** Install the required Python packages using `pip`:
   ```
   pip install -r requirements.txt
   ```

4. **Run the Development Server:** Start the development server:
   ```
   python server/server.py
   ```

5. **Access the Website:** 

    Open the `index.html` file in the **UI** folder on web browser to access the Website.

## Folder structure

* <b>UI : This contains ui website code</b> 
* <b>server: Contains the Python flask server related code</b>
* <b>model: Contains python notebook for model building</b>

## Technologies used in this project,

* `Python`
* `Numpy` and `OpenCV` for data cleaning
* `Matplotlib` & `Seaborn` for data visualization
* `Sklearn` for model building
* Python `flask` for http server
* `HTML`,`CSS`,`Javascript` for UI 

## Contributing

Contributions are welcome! If you'd like to contribute to the project, feel free to submit issues or pull requests. Please ensure your contributions align with the project's coding standards and guidelines.

## Repository Code Formatting

This repository follows a consistent code formatting approach to enhance readability and maintainability.

### Python Files

Python files in this repository are formatted using [Black](https://github.com/psf/black). Black is an opinionated code formatter that automatically formats your Python code to adhere to the PEP 8 style guide.

To ensure that your Python code is formatted correctly, you can install Black and format the code by running the following command in your terminal:

```bash
pip install black
black .
```

### HTML Files

HTML files in this repository are formatted using [Prettier](https://prettier.io/). Prettier is a code formatter that supports multiple languages, including HTML.

*Hope you like this project !!!*
