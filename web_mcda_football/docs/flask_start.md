Here's how you can create a Flask web application to display the top 5 football players ranked using the WASPAS method, based on the CLI code you provided.

The Flask app will render an HTML page showing the top 5 players in a table format.

### HTML Template (index.html)

Create a folder named `templates` in the same directory as your Flask app and add an `index.html` file with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Top 5 Players</title>
    <style>
        table {
            width: 80%;
            margin: 20px auto;
            border-collapse: collapse;
        }
        th, td {
            padding: 10px;
            border: 1px solid #ddd;
            text-align: center;
        }
        th {
            background-color: #f4f4f4;
        }
    </style>
</head>
<body>
    <h1 style="text-align: center;">Top 5 Football Players</h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Skill</th>
                <th>Pace</th>
                <th>Strength</th>
                <th>Age</th>
                <th>Cost</th>
                <th>WASPAS Score</th>
            </tr>
        </thead>
        <tbody>
            {% for player in players.iterrows() %}
            <tr>
                <td>{{ player[1]['Name'] }}</td>
                <td>{{ player[1]['Skill'] }}</td>
                <td>{{ player[1]['Pace'] }}</td>
                <td>{{ player[1]['Strength'] }}</td>
                <td>{{ player[1]['Age'] }}</td>
                <td>{{ player[1]['Cost'] }}</td>
                <td>{{ player[1]['WASPAS_Score'] }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
```

### Running the App
1. Save the Flask app and `index.html` file.
2. Run the Flask app: 
   ```bash
   python app.py
   ```
3. Open your browser and navigate to `http://127.0.0.1:5000/` to view the top 5 players.

Let me know if you'd like to refine this further!