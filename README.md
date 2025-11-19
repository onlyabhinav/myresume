# Online Resume Web App

A modern, minimalistic online resume built with Python Flask and ready for deployment on Back4App.

## Features

- Clean, professional design
- Responsive layout (mobile-friendly)
- Easy to customize
- Ready for Docker deployment
- Print-friendly styling

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to `http://localhost:5000`

## Customization

Edit the `resume_data` dictionary in `app.py` to customize your resume with your own information:

- Personal information (name, title, contact details)
- Professional summary
- Work experience
- Education
- Skills
- Projects

## Deploying to Back4App

### Prerequisites
- A GitHub account
- A Back4App account (sign up at https://www.back4app.com/)

### Steps:

1. **Push to GitHub**
   - Create a new repository on GitHub
   - Push this code to your repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/your-repo.git
   git push -u origin main
   ```

2. **Create a New App on Back4App**
   - Log in to Back4App
   - Click "Build new app"
   - Choose "Container as a Service"
   - Give your app a name

3. **Connect GitHub Repository**
   - Connect your GitHub account
   - Select the repository containing your resume app
   - Choose the branch (usually `main` or `master`)

4. **Configure Deployment**
   - Back4App will automatically detect your Dockerfile
   - Set the container port to `5000` (or use the default PORT environment variable)
   - Add any environment variables if needed

5. **Deploy**
   - Click "Deploy"
   - Wait for the build to complete
   - Your resume will be live at the URL provided by Back4App

### Environment Variables

Back4App automatically provides:
- `PORT` - The port your app should listen on

You can add custom environment variables through the Back4App dashboard if needed.

## Project Structure

```
.
├── app.py                  # Flask application
├── templates/
│   └── index.html         # HTML template
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── .dockerignore         # Docker ignore file
└── README.md            # This file
```

## Technologies Used

- **Python 3.11**
- **Flask** - Web framework
- **Gunicorn** - Production WSGI server
- **Docker** - Containerization

## Customizing the Design

The design is fully contained in the `<style>` section of `templates/index.html`. You can customize:

- Colors (see CSS variables in `:root`)
- Fonts
- Layout
- Spacing
- Responsive breakpoints

## License

Feel free to use this template for your own resume!
