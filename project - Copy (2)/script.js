// College Enquiry Chatbot JavaScript

class CollegeChatbot {
    constructor() {
        this.messageInput = document.getElementById('messageInput');
        this.sendButton = document.getElementById('sendButton');
        this.chatMessages = document.getElementById('chatMessages');
        this.typingIndicator = document.getElementById('typingIndicator');
        this.toastEl = document.getElementById('toast');


        this.initializeEventListeners();
        this.loadCollegeData();
        this.loadHistory();
        this.sendButton.disabled = this.messageInput.value.trim().length === 0;
    }

    initializeEventListeners() {
        this.sendButton.addEventListener('click', () => this.sendMessage());
        this.messageInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });
        this.messageInput.addEventListener('input', () => {
            const hasText = this.messageInput.value.trim().length > 0;
            this.sendButton.disabled = !hasText;
        });
        // Delegate copy-to-clipboard for any bot message copy buttons
        this.chatMessages.addEventListener('click', (e) => {
            const btn = e.target.closest('.copy-btn');
            if (!btn) return;
            const contentDiv = btn.closest('.message-content');
            if (!contentDiv) return;
            const textToCopy = contentDiv.innerText;
            navigator.clipboard.writeText(textToCopy).then(() => this.showToast('Copied response'));
        });
    }

    // Voice assistant logic removed

    loadCollegeData() {
        // College information database
        this.collegeData = {
            admissions: {
                keywords: ['admission', 'apply', 'application', 'eligibility', 'requirements', 'entrance'],
                response: `
                    <h4>Admission Requirements:</h4>
                    <ul>
                        <li><strong>Undergraduate:</strong> 12th grade with minimum 75% marks</li>
                        <li><strong>Postgraduate:</strong> Bachelor's degree with minimum 60% marks</li>
                        <li><strong>Entrance Exams:</strong> JEE Main, NEET, CAT (depending on course)</li>
                        <li><strong>Documents:</strong> Mark sheets, certificates, ID proof, photos</li>
                        <li><strong>Application Deadline:</strong> June 30th for most courses</li>
                    </ul>
                    <p>Would you like specific information about any particular course?</p>
                `
            },
            courses: {
                keywords: ['course', 'program', 'degree', 'study', 'curriculum', 'subjects'],
                response: `
                    <h4>Available Courses:</h4>
                    <ul>
                        <li><strong>Engineering:</strong> CSE, ECE, Mechanical, Civil, Chemical</li>
                        <li><strong>Medical:</strong> MBBS, BDS, Nursing, Pharmacy</li>
                        <li><strong>Management:</strong> MBA, BBA, Hotel Management</li>
                        <li><strong>Arts & Science:</strong> BA, BSc, MA, MSc in various specializations</li>
                        <li><strong>Law:</strong> LLB, LLM, Integrated Law Programs</li>
                        <li><strong>Commerce:</strong> BCom, MCom, CA, CS preparation</li>
                    </ul>
                    <p>Each program includes modern curriculum, practical training, and industry exposure.</p>
                `
            },
            fees: {
                keywords: ['fee', 'cost', 'tuition', 'payment', 'scholarship', 'financial'],
                response: `
                    <h4>Fee Structure (Annual):</h4>
                    <ul>
                        <li><strong>Engineering:</strong> ₹1,50,000 - ₹2,00,000</li>
                        <li><strong>Medical:</strong> ₹5,00,000 - ₹8,00,000</li>
                        <li><strong>Management:</strong> ₹1,20,000 - ₹1,80,000</li>
                        <li><strong>Arts & Science:</strong> ₹40,000 - ₹80,000</li>
                    </ul>
                    <h4>Scholarships Available:</h4>
                    <ul>
                        <li>Merit-based scholarships (up to 50% fee waiver)</li>
                        <li>Need-based financial assistance</li>
                        <li>Sports and cultural scholarships</li>
                        <li>Government scholarships for eligible students</li>
                    </ul>
                `
            },
            facilities: {
                keywords: ['facility', 'campus', 'hostel', 'library', 'lab', 'sports', 'accommodation'],
                response: `
                    <h4>Campus Facilities:</h4>
                    <ul>
                        <li><strong>Academic:</strong> Modern classrooms, well-equipped labs, digital library</li>
                        <li><strong>Accommodation:</strong> Separate hostels for boys and girls with Wi-Fi</li>
                        <li><strong>Sports:</strong> Cricket ground, basketball court, gym, swimming pool</li>
                        <li><strong>Dining:</strong> Multi-cuisine cafeteria with hygienic food</li>
                        <li><strong>Medical:</strong> 24/7 medical center with qualified doctors</li>
                        <li><strong>Transport:</strong> Bus service covering major city routes</li>
                        <li><strong>Technology:</strong> High-speed internet, smart classrooms</li>
                    </ul>
                `
            },
            placements: {
                keywords: ['placement', 'job', 'career', 'recruitment', 'company', 'salary'],
                response: `
                    <h4>Placement Statistics:</h4>
                    <ul>
                        <li><strong>Overall Placement Rate:</strong> 85%</li>
                        <li><strong>Average Package:</strong> ₹6.5 LPA</li>
                        <li><strong>Highest Package:</strong> ₹25 LPA</li>
                        <li><strong>Top Recruiters:</strong> TCS, Infosys, Wipro, Amazon, Google, Microsoft</li>
                    </ul>
                    <h4>Career Support:</h4>
                    <ul>
                        <li>Dedicated placement cell</li>
                        <li>Industry mentorship programs</li>
                        <li>Skill development workshops</li>
                        <li>Mock interviews and resume building</li>
                        <li>Internship opportunities</li>
                    </ul>
                `
            },
            contact: {
                keywords: ['contact', 'phone', 'email', 'address', 'location', 'visit'],
                response: `
                    <h4>Contact Information:</h4>
                    <ul>
                        <li><strong>Address:</strong> 123 Education Street, Knowledge City, State - 123456</li>
                        <li><strong>Phone:</strong> +91-9876543210</li>
                        <li><strong>Email:</strong> Contact college directly</li>
                        <li><strong>Website:</strong> Visit NSAKCET campus</li>
                        <li><strong>Office Hours:</strong> Mon-Fri: 9:00 AM - 5:00 PM</li>
                    </ul>
                    <p>You can also schedule a campus visit by calling our admission office!</p>
                `
            }
        };
    }

    async sendMessage() {
        const message = this.messageInput.value.trim();
        if (!message) return;

        // Add user message
        this.addMessage(message, 'user');
        this.messageInput.value = '';
        this.sendButton.disabled = true;

        // Show typing indicator
        this.showTypingIndicator();

        try {
            // Try to get response from backend first
            const response = await this.getAIResponse(message);
            this.hideTypingIndicator();
            this.addMessage(response, 'bot');
            this.saveHistory();
        } catch (error) {
            console.log('Backend unavailable, using local responses');
            this.showToast('Backend unavailable. Using offline mode.');
            // Fallback to local responses if backend is not available
            await this.delay(1500);
            const response = this.generateResponse(message);
            this.hideTypingIndicator();
            this.addMessage(response, 'bot');
            this.saveHistory();
        }
        
        this.sendButton.disabled = false;
        this.messageInput.focus();
    }

    addMessage(content, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;

        const avatarDiv = document.createElement('div');
        avatarDiv.className = 'message-avatar';
        avatarDiv.innerHTML = sender === 'user' ? '<i class="fas fa-user"></i>' : '<i class="fas fa-robot"></i>';

        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        if (sender === 'bot') {
            // Render HTML from backend responses
            contentDiv.innerHTML = content;
            const copyBtn = document.createElement('button');
            copyBtn.className = 'copy-btn';
            copyBtn.innerHTML = '<i class="fas fa-copy"></i>';
            copyBtn.title = 'Copy to clipboard';
            copyBtn.addEventListener('click', () => {
                const textToCopy = contentDiv.innerText;
                navigator.clipboard.writeText(textToCopy).then(() => this.showToast('Copied response'));
            });
            contentDiv.appendChild(copyBtn);
        } else {
            const p = document.createElement('p');
            p.textContent = content;
            contentDiv.appendChild(p);
        }

        messageDiv.appendChild(avatarDiv);
        messageDiv.appendChild(contentDiv);

        this.chatMessages.appendChild(messageDiv);
        this.scrollToBottom();
    }

    // Text-to-speech logic removed

    generateResponse(userMessage) {
        const message = userMessage.toLowerCase();
        
        // Check for greetings
        if (this.containsKeywords(message, ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening'])) {
            return "Hello! Welcome to our college enquiry system. I'm here to help you with any questions about admissions, courses, fees, facilities, or placements. What would you like to know?";
        }

        // Check for thanks
        if (this.containsKeywords(message, ['thank', 'thanks', 'appreciate'])) {
            return "You're welcome! I'm glad I could help. If you have any more questions about our college, feel free to ask anytime!";
        }

        // Check for goodbye
        if (this.containsKeywords(message, ['bye', 'goodbye', 'see you', 'exit'])) {
            return "Goodbye! Thank you for your interest in our college. We look forward to welcoming you to our campus soon. Have a great day!";
        }

        // Search through college data
        for (const [category, data] of Object.entries(this.collegeData)) {
            if (this.containsKeywords(message, data.keywords)) {
                return data.response;
            }
        }

        // Default response with suggestions
        return `
            I'd be happy to help you with information about our college! Here are some topics I can assist you with:
            <ul>
                <li><strong>Admissions:</strong> Requirements, applications, deadlines</li>
                <li><strong>Courses:</strong> Available programs and curriculum</li>
                <li><strong>Fees:</strong> Tuition costs and scholarships</li>
                <li><strong>Facilities:</strong> Campus amenities and services</li>
                <li><strong>Placements:</strong> Career opportunities and statistics</li>
                <li><strong>Contact:</strong> How to reach us</li>
            </ul>
            <p>Could you please be more specific about what you'd like to know?</p>
        `;
    }

    containsKeywords(message, keywords) {
        return keywords.some(keyword => message.includes(keyword));
    }

    showTypingIndicator() {
        this.typingIndicator.style.display = 'block';
        this.scrollToBottom();
    }

    hideTypingIndicator() {
        this.typingIndicator.style.display = 'none';
    }

    scrollToBottom() {
        this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
    }

    delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    async getAIResponse(message) {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });

        if (!response.ok) {
            throw new Error('Backend unavailable');
        }

        const data = await response.json();
        return data.response;
    }

    showToast(text) {
        if (!this.toastEl) return;
        this.toastEl.textContent = text;
        this.toastEl.classList.add('show');
        clearTimeout(this._toastTimer);
        this._toastTimer = setTimeout(() => {
            this.toastEl.classList.remove('show');
        }, 2000);
    }

    loadHistory() {
        try {
            const raw = localStorage.getItem('chat_history');
            if (!raw) return;
            const items = JSON.parse(raw);
            if (Array.isArray(items) && items.length > 0) {
                this.chatMessages.innerHTML = '';
                items.forEach(item => this.addMessage(item.content, item.sender));
            }
        } catch (_) {}
    }

    saveHistory() {
        const messages = Array.from(this.chatMessages.querySelectorAll('.message'));
        const data = messages.map(msg => {
            const isUser = msg.classList.contains('user-message');
            const contentEl = msg.querySelector('.message-content');
            let content;
            if (isUser) {
                content = contentEl.innerText;
            } else {
                // Strip utility controls before saving
                const clone = contentEl.cloneNode(true);
                const btn = clone.querySelector('.copy-btn');
                if (btn) btn.remove();
                content = clone.innerHTML;
            }
            return { sender: isUser ? 'user' : 'bot', content };
        });
        try {
            localStorage.setItem('chat_history', JSON.stringify(data));
        } catch (_) {}
    }

    clearChat() {
        this.chatMessages.innerHTML = '';
        localStorage.removeItem('chat_history');
        this.showToast('Chat cleared');
    }

    exportChat() {
        const messages = Array.from(this.chatMessages.querySelectorAll('.message'));
        if (messages.length === 0) {
            this.showToast('Nothing to export');
            return;
        }
        const lines = messages.map(msg => {
            const role = msg.classList.contains('user-message') ? 'You' : 'Assistant';
            const text = msg.querySelector('.message-content').innerText.trim();
            return `${role}: ${text}`;
        });
        const blob = new Blob([lines.join('\n\n')], { type: 'text/plain;charset=utf-8' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `nsakcet-chat-${Date.now()}.txt`;
        document.body.appendChild(a);
        a.click();
        URL.revokeObjectURL(url);
        a.remove();
    }
}

// Quick message function
function sendQuickMessage(message) {
    const chatbot = window.chatbot;
    chatbot.messageInput.value = message;
    chatbot.sendMessage();
}

// Initialize chatbot when page loads
document.addEventListener('DOMContentLoaded', () => {
    window.chatbot = new CollegeChatbot();
    const clearBtn = document.getElementById('clearButton');
    const exportBtn = document.getElementById('exportButton');
    if (clearBtn) clearBtn.addEventListener('click', () => window.chatbot.clearChat());
    if (exportBtn) exportBtn.addEventListener('click', () => window.chatbot.exportChat());
});
