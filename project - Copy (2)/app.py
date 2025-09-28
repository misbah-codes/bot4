from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
import re
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)

class CollegeEnquiryBot:
    def __init__(self):
        self.college_data = {
            "college_info": {
                "name": "Nawab Shah Alam Khan College of Engineering and Technology (NSAKCET)",
                "established": "2008",
                "location": "Old Malakpet, Hyderabad, Telangana",
                "type": "Private, Un-aided Engineering Institution",
                "accreditation": "AICTE Approved, NAAC Accredited, Affiliated to Osmania University (Autonomous), UGC 2F Recognition",
                "society": "Sultan ul Uloom Educational Society",
                "campus_size": "5 acres",
                "accessibility": "Centrally located, few hundred meters from railway station, metro station, and bus depot"
            },
            "courses": {
                "undergraduate": {
                    "engineering": [
                        {"name": "Computer Science & Engineering (CSE)", "duration": "4 years", "seats": "~120", "fee": 247000, "rca_fee": 247000},
                        {"name": "CSE (Artificial Intelligence & Machine Learning)", "duration": "4 years", "seats": "~60", "fee": 290000, "rca_fee": 247000},
                        {"name": "CSE (Data Science)", "duration": "4 years", "seats": "~60", "fee": 290000, "rca_fee": 247000},
                        {"name": "CSE (IoT & Cybersecurity - Blockchain)", "duration": "4 years", "seats": "~60", "fee": 290000, "rca_fee": 247000},
                        {"name": "Information Technology (IT)", "duration": "4 years", "seats": "~60", "fee": 247000, "rca_fee": 247000},
                        {"name": "Mechanical Engineering", "duration": "4 years", "seats": "~120", "fee": 247000, "rca_fee": 247000},
                        {"name": "Civil Engineering", "duration": "4 years", "seats": "~120", "fee": 247000, "rca_fee": 247000},
                        {"name": "Electrical & Electronics Engineering (EEE)", "duration": "4 years", "seats": "~60", "fee": 247000, "rca_fee": 247000}
                    ]
                },
                "diploma": {
                    "programs": [
                        {"name": "Mechanical Engineering Diploma", "duration": "3 years", "seats": "~48", "fee": 44700},
                        {"name": "Civil Engineering Diploma", "duration": "3 years", "seats": "~48", "fee": 44700},
                        {"name": "Electrical & Electronics Engineering Diploma", "duration": "3 years", "seats": "~48", "fee": 44700},
                        {"name": "Electronics & Communication Engineering Diploma", "duration": "3 years", "seats": "~48", "fee": 44700},
                        {"name": "Computer Science Engineering Diploma", "duration": "3 years", "seats": "~48", "fee": 44700},
                        {"name": "Artificial Intelligence", "duration": "3 years", "seats": "~48", "fee": 44700}
                    ]
                },
                "total_intake": {
                    "b.e": "~720 seats",
                    "diploma": "~240 seats"
                }
            },
            "admission_process": {
                "b.e_eligibility": "10+2 with minimum 45% marks",
                "diploma_eligibility": "10th pass",
                "entrance_exams": {
                    "b.e": ["TS EAMCET (Primary)", "JEE Main (Alternative)"],
                    "diploma": ["TS POLYCET"]
                },
                "selection_criteria": "TS EAMCET Rank for B.Tech, TS POLYCET for Diploma",
                "fee_structure": {
                    "b.e_regular": "₹2.47 lakh (RCA fee for most branches)",
                    "b.e_emerging": "₹2.4-2.9 lakh (AI/ML, Data Science, IoT branches)",
                    "diploma": "₹44,700 approximately"
                },
                "documents_required": [
                    "SSC & Intermediate mark sheets",
                    "TS EAMCET / JEE Main scorecard",
                    "Transfer certificate",
                    "Study certificate",
                    "Caste certificate (if applicable)",
                    "Income certificate (for scholarships)",
                    "Passport size photographs"
                ]
            },
            "facilities": {
                "academic": [
                    "Digitally enabled spacious classrooms",
                    "Computer labs and electronics/engineering labs",
                    "Language lab",
                    "Library (note: some outdated resources reported)",
                    "Wi-Fi connectivity (100 Mbps dedicated bandwidth)",
                    "Seminar halls"
                ],
                "infrastructure": [
                    "Aesthetic buildings on 5-acre landscaped campus",
                    "Auditorium for events and presentations",
                    "Canteen with food facilities",
                    "Medical facilities on campus",
                    "ATM and bank counters",
                    "Backup power supply (200 kVA DG set)",
                    "Disabled-friendly infrastructure"
                ],
                "recreational": [
                    "Playground for sports activities",
                    "Gymnasium facilities",
                    "Campus events and cultural activities"
                ],
                "accommodation": {
                    "hostel": "No hostel facility provided due to central urban location",
                    "advantage": "Centrally located - easy commute from anywhere in Hyderabad",
                    "transport": "Near railway station, metro station, and bus depot"
                }
            },
            "placements": {
                "statistics": {
                    "overall_rate": "65-70% placement rate",
                    "package_range": "₹3 LPA to ₹6-8 LPA typically",
                    "highest_package": "₹12 LPA (rare cases, some reports mention ₹75 LPA)",
                    "average_package": "₹6 LPA",
                    "internship_rate": "Around 80% internship opportunities"
                },
                "branch_specific": {
                    "cse_ai_ml": "70% placement rate, highest ₹75 LPA, lowest ₹3 LPA",
                    "civil_2023": "70% placement rate, highest ₹12 LPA, lowest ₹3 LPA, average ₹6 LPA",
                    "mechanical_diploma": "Average ₹2-2.5 LPA, top ₹4.2 LPA"
                },
                "top_recruiters": [
                    "Amazon", "Microsoft", "IBM", "Tata", "L&T", 
                    "Tech Mahindra", "Cisco", "Wipro", "BHEL", "TAFE", "Byju's", "TVS"
                ],
                "placement_support": [
                    "Placement activities recently ramped up",
                    "Internship opportunities with major companies",
                    "Students placed in engineer and supervisor roles",
                    "Career guidance and placement assistance"
                ],
                "note": "Placement activities have been ramped up recently with improving outcomes"
            },
            "student_feedback": {
                "overall_rating": "3.1-3.2 out of 5 on Shiksha",
                "category_ratings": {
                    "infrastructure": "3.4/5",
                    "faculty": "3.3/5",
                    "placements": "2.8/5",
                    "campus_life": "3.5/5",
                    "value_for_money": "3.2/5"
                },
                "pros": [
                    "Central location with excellent connectivity",
                    "Decent infrastructure and facilities",
                    "Responsive and student-friendly faculty",
                    "Management perceived as student-friendly",
                    "Gradually improving placement record",
                    "Easy commute from anywhere in Hyderabad"
                ],
                "cons": [
                    "No hostel facility (due to urban location)",
                    "Wi-Fi can be slow at times",
                    "Some library resources reported as outdated",
                    "Relatively few recruitment drives in some departments",
                    "Uneven teaching quality in certain cases",
                    "Limited campus-based residential facilities"
                ]
            },
            "scholarships": [
                {"name": "Merit-based Scholarships", "criteria": "Academic excellence", "benefit": "Fee concessions available"},
                {"name": "Government Scholarships", "criteria": "As per government norms", "benefit": "Fee reimbursement schemes"},
                {"name": "Financial Assistance", "criteria": "Economically weaker sections", "benefit": "Support for deserving students"}
            ]
        }
        
        self.conversation_context = []
        
    def preprocess_query(self, query):
        """Clean and normalize the user query"""
        query = query.lower().strip()
        # Remove extra spaces and punctuation
        query = re.sub(r'[^\w\s]', ' ', query)
        query = re.sub(r'\s+', ' ', query)
        return query
    
    def extract_intent(self, query):
        """Determine the user's intent from the query"""
        intents = {
            'greeting': ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening'],
            'admission': ['admission', 'apply', 'application', 'eligibility', 'entrance', 'how to apply'],
            'courses': ['course', 'program', 'degree', 'branch', 'stream', 'curriculum', 'syllabus'],
            'fees': ['fee', 'cost', 'tuition', 'payment', 'expensive', 'cheap', 'money'],
            'facilities': ['facility', 'hostel', 'library', 'lab', 'sports', 'gym', 'campus'],
            'placements': ['placement', 'job', 'career', 'salary', 'package', 'recruitment', 'company'],
            'scholarships': ['scholarship', 'financial aid', 'discount', 'waiver', 'assistance'],
            'location': ['address', 'location', 'where', 'situated', 'campus location'],
            'contact': ['contact', 'phone', 'email', 'reach', 'call'],
            'thanks': ['thank', 'thanks', 'appreciate', 'grateful'],
            'goodbye': ['bye', 'goodbye', 'see you', 'exit', 'quit']
        }

        # Always check for greeting intent first
        for intent, keywords in intents.items():
            if intent == 'greeting' and any(keyword in query for keyword in keywords):
                return intent

        # Refined off-topic/negative detection
        negative_patterns = [
            r'\b(hate|worst|bad|useless|stupid|dumb|idiot|boring|nonsense|irrelevant|silly|meaningless|no|never|nothing|don\'t care|who cares|not related|unrelated)\b',
            r'\b(joke|funny|laugh|lol|lmao|rofl|meme|prank|troll)\b',
            r'\b(weather|politics|movie|actor|actress|game|sports|food|restaurant|song|music|pet|dog|cat|car|bike|travel|holiday|vacation|birthday|married|single|love|crush|friend|family|parents|children|kids|salary|money|rich|poor|government|prime minister|president|minister|celebrity|famous|star)\b',
            r'\b(what is life|why am i here|who am i|what is the meaning of life|existence|philosophy)\b',
            r'\b(personal question|personal info|your name|who are you|where do you live|how old are you|are you human|are you robot|do you have feelings|do you love me|will you marry me)\b'
        ]
        for pattern in negative_patterns:
            if re.search(pattern, query):
                return 'off_topic'

        # If the query does not mention any college/education-related keywords, treat as off-topic
        topic_keywords = [
            'college', 'nsakcet', 'admission', 'course', 'program', 'degree', 'branch', 'syllabus', 'fee', 'tuition', 'facility', 'hostel', 'library', 'lab', 'campus', 'placement', 'job', 'career', 'scholarship', 'location', 'contact', 'faculty', 'student', 'review', 'rating', 'infrastructure', 'engineering', 'diploma', 'b.e', 'polytechnic', 'osmania', 'university'
        ]
        if not any(word in query for word in topic_keywords):
            return 'off_topic'

        # Check other intents
        for intent, keywords in intents.items():
            if any(keyword in query for keyword in keywords):
                return intent

        return 'general'
    
    def generate_response(self, query, intent):
        """Generate appropriate response based on intent"""
        responses = {
            'greeting': [
                "Hello! Welcome to Nawab Shah Alam Khan College of Engineering and Technology (NSAKCET). I'm here to help you with any questions about our college. What would you like to know?",
                "Hi there! I'm your NSAKCET enquiry assistant. Feel free to ask me about admissions, courses, facilities, placements, or anything else about our college!",
                "Good day! How can I assist you with your NSAKCET enquiry today?"
            ],
            'thanks': [
                "You're welcome! I'm glad I could help. Feel free to ask if you have any more questions!",
                "Happy to help! Is there anything else you'd like to know about our college?",
                "My pleasure! Don't hesitate to reach out if you need more information."
            ],
            'goodbye': [
                "Goodbye! Thank you for your interest in Nawab Shah Alam Khan College of Engineering and Technology (NSAKCET). We look forward to welcoming you!",
                "See you later! Best of luck with your college search. We'd love to have you join our NSAKCET community!",
                "Take care! Feel free to come back anytime if you have more questions about NSAKCET."
            ],
            'off_topic': [
                "I'm here to assist you with NSAKCET college-related queries. For other topics, please consult the appropriate resources.",
                "Sorry, I can only answer questions about Nawab Shah Alam Khan College of Engineering and Technology, its admissions, courses, and campus life.",
                "My expertise is limited to NSAKCET college information. Please ask something related to the college, and I'll be happy to help!",
                "It seems your question is not related to NSAKCET or education. Please ask about our college, and I'll do my best to assist you."
            ]
        }

        if intent in responses:
            return random.choice(responses[intent])

        # Generate specific responses based on intent
        if intent == 'admission':
            return self.get_admission_info(query)
        elif intent == 'courses':
            return self.get_course_info(query)
        elif intent == 'fees':
            return self.get_fee_info(query)
        elif intent == 'facilities':
            return self.get_facility_info(query)
        elif intent == 'placements':
            return self.get_placement_info(query)
        elif intent == 'scholarships':
            return self.get_scholarship_info()
        elif intent == 'location' or intent == 'contact':
            return self.get_contact_info()
        elif 'review' in query or 'rating' in query or 'student' in query or 'feedback' in query:
            return self.get_student_feedback()
        else:
            return self.get_general_info()
    
    def get_admission_info(self, query):
        admission = self.college_data['admission_process']
        response = f"""
        <h4>📚 NSAKCET Admission Information</h4>
        
        <p><strong>B.E Eligibility:</strong> {admission['b.e_eligibility']}</p>
        <p><strong>Diploma Eligibility:</strong> {admission['diploma_eligibility']}</p>
        
        <p><strong>Entrance Exams:</strong></p>
        <ul>
            <li><strong>B.E:</strong> {', '.join(admission['entrance_exams']['b.e'])}</li>
            <li><strong>Diploma:</strong> {', '.join(admission['entrance_exams']['diploma'])}</li>
        </ul>
        
        <p><strong>Selection Criteria:</strong> {admission['selection_criteria']}</p>
        
        <p><strong>Fee Structure:</strong></p>
        <ul>
            <li><strong>B.E (Regular):</strong> {admission['fee_structure']['b.e_regular']}</li>
            <li><strong>B.E (Emerging):</strong> {admission['fee_structure']['b.e_emerging']}</li>
            <li><strong>Diploma:</strong> {admission['fee_structure']['diploma']}</li>
        </ul>
        
        <p><strong>Required Documents:</strong></p>
        <ul>
        """
        for doc in admission['documents_required']:
            response += f"<li>{doc}</li>"
        response += "</ul><p>NSAKCET offers ~720 B.Tech seats and ~240 Diploma seats. Would you like specific information about any particular course?</p>"
        
        return response
    
    def get_course_info(self, query):
        courses = self.college_data['courses']
        response = "<h4>🎓 NSAKCET Available Courses</h4>"
        
        # Check if user is asking about specific course type
        if 'diploma' in query or 'polytechnic' in query:
            response += "<h5>Diploma Programs (3 years):</h5><ul>"
            for course in courses['diploma']['programs']:
                response += f"<li><strong>{course['name']}</strong> - {course['duration']}, {course['seats']} seats, ₹{course['fee']:,}/year</li>"
            response += f"</ul><p><strong>Total Diploma Intake:</strong> {courses['total_intake']['diploma']}</p>"
        elif 'be' in query or 'b.e' in query or 'engineering' in query or 'cse' in query or 'ai' in query or 'data science' in query:
            response += "<h5>B.E Programs (4 years):</h5><ul>"
            for course in courses['undergraduate']['engineering']:
                fee_display = f"₹{course['fee']:,}" if course['fee'] == course['rca_fee'] else f"₹{course['fee']:,} (RCA: ₹{course['rca_fee']:,})"
                response += f"<li><strong>{course['name']}</strong> - {course['duration']}, {course['seats']} seats, {fee_display}/year</li>"
            response += f"</ul><p><strong>Total B.E Intake:</strong> {courses['total_intake']['b.e']}</p>"
        else:
            # Show overview of all courses
            response += "<h5>B.E Engineering Programs:</h5><ul>"
            for course in courses['undergraduate']['engineering'][:4]:
                response += f"<li><strong>{course['name']}</strong> - {course['seats']} seats</li>"
            response += "</ul><h5>Diploma Programs:</h5><ul>"
            for course in courses['diploma']['programs'][:3]:
                response += f"<li><strong>{course['name']}</strong> - {course['seats']} seats</li>"
            response += f"</ul><p><strong>Total Intake:</strong> {courses['total_intake']['b.e']} + {courses['total_intake']['diploma']}</p>"
            response += "<p>Ask me about specific programs like 'CSE AI/ML', 'diploma courses', or 'B.Tech fees' for detailed information!</p>"
        
        return response
    
    def get_fee_info(self, query):
        courses = self.college_data['courses']
        admission = self.college_data['admission_process']
        response = "<h4>💰 NSAKCET Fee Structure (Annual)</h4>"
        
        response += "<h5>B.Tech Programs (4 years):</h5><ul>"
        for course in courses['undergraduate']['engineering']:
            if course['fee'] == course['rca_fee']:
                response += f"<li><strong>{course['name']}</strong>: ₹{course['fee']:,} (RCA Fee)</li>"
            else:
                response += f"<li><strong>{course['name']}</strong>: ₹{course['fee']:,} (RCA: ₹{course['rca_fee']:,})</li>"
        response += "</ul>"
        
        response += "<h5>Diploma Programs (3 years):</h5><ul>"
        for course in courses['diploma']['programs']:
            response += f"<li><strong>{course['name']}</strong>: ₹{course['fee']:,}</li>"
        response += "</ul>"
        
        response += "<h5>Fee Summary:</h5><ul>"
        response += f"<li><strong>B.E Regular Programs:</strong> {admission['fee_structure']['b.e_regular']}</li>"
        response += f"<li><strong>B.E Emerging Programs:</strong> {admission['fee_structure']['b.e_emerging']}</li>"
        response += f"<li><strong>Diploma Programs:</strong> {admission['fee_structure']['diploma']}</li>"
        response += "</ul>"
        
        response += f"<p><strong>Total Intake:</strong> {courses['total_intake']['b.e']} + {courses['total_intake']['diploma']}</p>"
        response += "<p><em>Note: RCA (Reimbursement of Course fee under Admission) - Government fee reimbursement scheme available for eligible students.</em></p>"
        
        return response
    
    def get_facility_info(self, query):
        facilities = self.college_data['facilities']
        college_info = self.college_data['college_info']
        response = f"<h4>🏦 NSAKCET Campus Facilities</h4>"
        
        response += f"<p><strong>Campus:</strong> {college_info['campus_size']} with aesthetic buildings and landscaped grounds</p>"
        response += f"<p><strong>Location Advantage:</strong> {college_info['accessibility']}</p>"
        
        response += "<h5>Academic Facilities:</h5><ul>"
        for facility in facilities['academic']:
            response += f"<li>{facility}</li>"
        response += "</ul>"
        
        response += "<h5>Infrastructure & Amenities:</h5><ul>"
        for facility in facilities['infrastructure']:
            response += f"<li>{facility}</li>"
        response += "</ul>"
        
        response += "<h5>Sports & Recreation:</h5><ul>"
        for facility in facilities['recreational']:
            response += f"<li>{facility}</li>"
        response += "</ul>"
        
        response += "<h5>Accommodation Information:</h5>"
        response += f"<p><strong>Hostel:</strong> {facilities['accommodation']['hostel']}</p>"
        response += f"<p><strong>Advantage:</strong> {facilities['accommodation']['advantage']}</p>"
        response += f"<p><strong>Transport:</strong> {facilities['accommodation']['transport']}</p>"
        
        return response
    
    def get_placement_info(self, query):
        placements = self.college_data['placements']
        stats = placements['statistics']
        
        response = f"""
        <h4>🚀 NSAKCET Placement Statistics</h4>
        <ul>
            <li><strong>Placement Rate:</strong> {stats['overall_rate']}</li>
            <li><strong>Package Range:</strong> {stats['package_range']}</li>
            <li><strong>Average Package:</strong> {stats['average_package']}</li>
            <li><strong>Highest Package:</strong> {stats['highest_package']}</li>
            <li><strong>Internship Rate:</strong> {stats['internship_rate']}</li>
        </ul>
        
        <h5>Branch-wise Performance:</h5>
        <ul>
            <li><strong>CSE AI/ML:</strong> {placements['branch_specific']['cse_ai_ml']}</li>
            <li><strong>Civil (2023):</strong> {placements['branch_specific']['civil_2023']}</li>
            <li><strong>Mechanical Diploma:</strong> {placements['branch_specific']['mechanical_diploma']}</li>
        </ul>
        
        <h5>Top Recruiters:</h5>
        <p>{', '.join(placements['top_recruiters'][:10])}</p>
        
        <h5>Placement Support:</h5>
        <ul>
        """
        for support in placements['placement_support']:
            response += f"<li>{support}</li>"
        response += f"</ul><p><em>Note:</em> {placements['note']}</p>"
        
        return response
    
    def get_scholarship_info(self):
        scholarships = self.college_data['scholarships']
        response = "<h4>🎯 NSAKCET Scholarship Opportunities</h4><ul>"
        
        for scholarship in scholarships:
            response += f"<li><strong>{scholarship['name']}</strong>: {scholarship['criteria']} - {scholarship['benefit']}</li>"
        response += "</ul><p>Contact the college admission office for detailed eligibility criteria and application process.</p>"
        
        return response
    
    def get_student_feedback(self):
        feedback = self.college_data['student_feedback']
        response = f"""
        <h4>📊 Student Reviews & Ratings</h4>
        <p><strong>Overall Rating:</strong> {feedback['overall_rating']}</p>
        
        <h5>Category-wise Ratings:</h5>
        <ul>
            <li><strong>Infrastructure:</strong> {feedback['category_ratings']['infrastructure']}</li>
            <li><strong>Faculty:</strong> {feedback['category_ratings']['faculty']}</li>
            <li><strong>Placements:</strong> {feedback['category_ratings']['placements']}</li>
            <li><strong>Campus Life:</strong> {feedback['category_ratings']['campus_life']}</li>
            <li><strong>Value for Money:</strong> {feedback['category_ratings']['value_for_money']}</li>
        </ul>
        
        <h5>Student Highlights (Pros):</h5>
        <ul>
        """
        for pro in feedback['pros']:
            response += f"<li>{pro}</li>"
        
        response += "</ul><h5>Areas for Improvement (Cons):</h5><ul>"
        for con in feedback['cons']:
            response += f"<li>{con}</li>"
        
        response += "</ul><p><em>Reviews are based on actual student feedback from Shiksha.com</em></p>"
        
        return response
    
    def get_contact_info(self):
        college = self.college_data['college_info']
        return f"""
        <h4>📞 Contact Information</h4>
        <ul>
            <li><strong>College:</strong> {college['name']}</li>
            <li><strong>Address:</strong> {college['location']}</li>
            <li><strong>Accessibility:</strong> {college['accessibility']}</li>
            <li><strong>Campus Size:</strong> {college['campus_size']}</li>
            <li><strong>Managed by:</strong> {college['society']}</li>
            <li><strong>Accreditation:</strong> {college['accreditation']}</li>
        </ul>
        <p><strong>Location Advantage:</strong> Centrally located for easy commute from anywhere in Hyderabad - near railway station, metro station, and bus depot.</p>
        <p>For admission inquiries, please contact the college directly or visit the campus.</p>
        """
    
    def get_general_info(self):
        college = self.college_data['college_info']
        return f"""
        <h4>🏛️ About {college['name']}</h4>
        <p>Established in {college['established']}, we are a {college['type']} institution with {college['accreditation']}.</p>
        
        <p>I can help you with information about:</p>
        <ul>
            <li><strong>Admissions:</strong> Requirements, process, and deadlines</li>
            <li><strong>Courses:</strong> Available programs and curriculum</li>
            <li><strong>Fees:</strong> Tuition costs and payment options</li>
            <li><strong>Facilities:</strong> Campus amenities and services</li>
            <li><strong>Placements:</strong> Career opportunities and statistics</li>
            <li><strong>Scholarships:</strong> Financial aid and assistance</li>
        </ul>
        <p>What specific information would you like to know?</p>
        """

# Initialize the chatbot
chatbot = CollegeEnquiryBot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Empty message'}), 400
        
        # Process the message
        processed_query = chatbot.preprocess_query(user_message)
        intent = chatbot.extract_intent(processed_query)
        response = chatbot.generate_response(processed_query, intent)
        
        # Add to conversation context
        chatbot.conversation_context.append({
            'user': user_message,
            'bot': response,
            'timestamp': datetime.now().isoformat(),
            'intent': intent
        })
        
        # Keep only last 10 conversations for context
        if len(chatbot.conversation_context) > 10:
            chatbot.conversation_context = chatbot.conversation_context[-10:]
        
        return jsonify({
            'response': response,
            'intent': intent,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    print("College Enquiry Chatbot Server Starting...")
    print("Loaded college data and AI responses")
    print("Server will be available at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
