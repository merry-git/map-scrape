# Google Maps Places API Python Script

This Python script allows you to search for places using the Google Maps Places API and retrieve essential information about those places, such as name, phone number, and user ratings. It's a handy tool for finding various types of businesses or services in a specific city or area.

## Prerequisites

Before using this script, you need to have the following:

- Python installed on your system.
- A valid Google Maps API Key. You can obtain one by following [Google's API Key documentation](https://developers.google.com/maps/gmp-get-started#enable-apis).

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/google-maps-places-api-python.git
   cd google-maps-places-api-python
   ```

2. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open the `main.py` file in a text editor or IDE.

2. Replace `"YOUR_API_KEY"` in the `api_key` variable with your Google Maps API Key.

3. Run the script in your terminal:

   ```bash
   python main.py
   ```

4. Follow the prompts to input your search parameters:
   - Enter the city or area you want to search.
   - Choose a type of service to search for (e.g., 'restaurant', 'gym', 'cafe').
   - Enter the maximum number of results you want (note that a maximum of 20 results can be retrieved per iteration).

5. The script will provide you with a list of places found, including their names, phone numbers, and user ratings (if available). The results will be organized by restaurant name.

## Supported Types

The script supports a variety of service types, including 'restaurant', 'gym', 'cafe', 'car_repair', and more. You can find a full list of supported types in the [Google Maps Places API documentation](https://developers.google.com/maps/documentation/places/web-service/supported_types).

## Customization

You can customize the script by modifying the `field_mapping` and `fields` variables to include additional fields or change the information you want to retrieve.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Feel free to replace `"YOUR_API_KEY"` with the actual API key and modify the README content further to suit your preferences. Make sure to include your project's license information as well.

Once you have created this README file in your GitHub repository, users will have clear instructions on how to use your code and what prerequisites are required.
