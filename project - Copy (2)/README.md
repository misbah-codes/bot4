# AI-Based College Enquiry Chatbot

A modern, intelligent chatbot designed to help prospective students get information about college admissions, courses, fees, facilities, and placements.

## Features

- 🤖 **AI-Powered Responses**: Intelligent natural language processing for accurate answers
- 💬 **Interactive Chat Interface**: Modern, responsive web-based chat UI
- 📚 **Comprehensive Information**: Covers admissions, courses, fees, facilities, placements, and scholarships
- 🎯 **Quick Actions**: Pre-defined buttons for common queries
- 📱 **Mobile Responsive**: Works seamlessly on desktop and mobile devices
- 🔄 **Real-time Responses**: Instant answers with typing indicators
- 🎨 **Beautiful UI**: Modern gradient design with smooth animations

## Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Python Flask
- **AI/NLP**: Custom intent recognition and response generation
- **Styling**: CSS Grid/Flexbox with modern animations
- **Icons**: Font Awesome

## Installation & Setup

1. **Clone or download the project**
   ```bash
   cd project
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask server**
   ```bash
   python app.py
   ```

4. **Open your browser and navigate to**
   ```
   http://localhost:5000
   ```

## Project Structure

```
project/
├── app.py                 # Flask backend server
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── styles.css        # CSS styling
    └── script.js         # JavaScript functionality
```

## Features Overview

### 🎓 College Information
- Institution details and accreditation
- Campus location and contact information
- Establishment history and achievements

### 📝 Admissions
- Admission requirements and eligibility criteria
- Entrance exam information (JEE, NEET, CAT, etc.)
- Application process and deadlines
- Required documents checklist

### 📚 Courses & Programs
- Undergraduate and postgraduate programs
- Engineering, Medical, Management courses
- Course duration, seats, and curriculum details
- Specialization options

### 💰 Fees & Scholarships
- Detailed fee structure for all courses
- Scholarship opportunities and eligibility
- Financial aid and payment options
- Merit and need-based assistance

### 🏫 Campus Facilities
- Academic facilities (labs, library, classrooms)
- Residential facilities (hostels, mess)
- Sports and recreational amenities
- Technology infrastructure

### 🚀 Placements & Careers
- Placement statistics and success rates
- Top recruiting companies
- Average and highest salary packages
- Career support and training programs

## How It Works

1. **User Input**: Students type their questions in natural language
2. **Intent Recognition**: AI analyzes the query to understand user intent
3. **Response Generation**: System generates relevant, detailed responses
4. **Interactive Display**: Information is presented in a user-friendly format

## Customization

### Adding New Information
Edit the `college_data` dictionary in `app.py` to update:
- Course details and fees
- Facility information
- Placement statistics
- Contact information

### Modifying UI
- Update `static/styles.css` for visual changes
- Modify `templates/index.html` for structure changes
- Edit `static/script.js` for functionality updates

### Extending AI Capabilities
- Add new intents in the `extract_intent()` method
- Create corresponding response methods
- Update keyword matching for better accuracy

## Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Mobile Support

Fully responsive design that works on:
- Smartphones (iOS/Android)
- Tablets
- Desktop computers

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Support

For technical support or questions about NSAKCET:
- Visit: Old Malakpet, Hyderabad, Telangana
- Contact: College admission office directly

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Built with ❤️ for better student experience**
