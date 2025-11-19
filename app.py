from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Resume data
    resume_data = {
        'name': 'Your Name',
        'title': 'Full Stack Developer',
        'location': 'Nagpur, Maharashtra, India',
        'email': 'your.email@example.com',
        'phone': '+91 XXX XXX XXXX',
        'linkedin': 'linkedin.com/in/yourprofile',
        'github': 'github.com/yourusername',
        'summary': 'Passionate software developer with expertise in building scalable web applications. Experienced in modern technologies and committed to writing clean, maintainable code.',
        'experience': [
            {
                'title': 'Senior Software Engineer',
                'company': 'Tech Company Inc.',
                'period': '2022 - Present',
                'description': [
                    'Led development of microservices architecture serving 1M+ users',
                    'Implemented CI/CD pipelines reducing deployment time by 60%',
                    'Mentored junior developers and conducted code reviews'
                ]
            },
            {
                'title': 'Software Engineer',
                'company': 'Startup Solutions',
                'period': '2020 - 2022',
                'description': [
                    'Developed RESTful APIs using Python and Flask',
                    'Optimized database queries improving performance by 40%',
                    'Collaborated with cross-functional teams in Agile environment'
                ]
            }
        ],
        'education': [
            {
                'degree': 'Bachelor of Technology in Computer Science',
                'institution': 'University Name',
                'period': '2016 - 2020',
                'details': 'CGPA: 8.5/10'
            }
        ],
        'skills': {
            'Languages': ['Python', 'JavaScript', 'Java', 'SQL'],
            'Frameworks': ['Flask', 'Django', 'React', 'Node.js'],
            'Tools': ['Docker', 'Git', 'AWS', 'PostgreSQL', 'MongoDB'],
            'Other': ['REST APIs', 'Microservices', 'CI/CD', 'Agile/Scrum']
        },
        'projects': [
            {
                'name': 'E-commerce Platform',
                'description': 'Built a full-stack e-commerce application with payment integration',
                'technologies': 'Python, Flask, React, PostgreSQL',
                'link': 'github.com/yourusername/project'
            },
            {
                'name': 'Task Management System',
                'description': 'Real-time collaborative task manager with WebSocket support',
                'technologies': 'Node.js, Socket.io, MongoDB',
                'link': 'github.com/yourusername/project2'
            }
        ]
    }
    
    return render_template('index.html', data=resume_data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
