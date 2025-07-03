# EA Exam Practice Application

A comprehensive Enrolled Agent (EA) exam preparation tool featuring 1000+ practice questions across all three parts of the Special Enrollment Examination (SEE). This application provides both unlimited practice mode and official exam simulation to help candidates prepare for the EA certification.

## 🎯 Features

### Practice Mode
- **1000+ Questions**: Comprehensive question bank covering all EA exam topics
- **Unlimited Time**: Study at your own pace without time pressure
- **Instant Feedback**: Immediate explanations for correct and incorrect answers
- **Progress Tracking**: Monitor your performance across categories and difficulty levels
- **Question Flagging**: Mark questions for later review
- **Export Functionality**: Download flagged questions and incorrect answers for offline study

### Simulation Exam
- **Official Structure**: Three-part exam matching real EA exam format
- **Timed Experience**: 3.5 hours per part (10.5 hours total)
- **Part-by-Part Navigation**: Complete parts independently within 2-year window
- **Progress Analytics**: Track answered questions, time spent, and flagged items
- **Results Export**: Download complete simulation results and performance data

### Official EA Exam Information
- **Complete Study Guide**: Prometric testing details and requirements
- **Content Breakdown**: 25+ detailed topics per exam part
- **Study Materials**: Official IRS publications and recommended resources
- **Post-Exam Process**: Form 23 application and enrollment procedures
- **Continuing Education**: 72-hour requirement every 3 years

## 📚 Exam Structure

| Part | Subject | Questions | Time Limit | Passing Score |
|------|---------|-----------|------------|---------------|
| Part 1 | Individual Tax | 100 | 3.5 hours | 75% (105/130) |
| Part 2 | Business Tax | 100 | 3.5 hours | 75% (105/130) |
| Part 3 | Ethics & Procedures | 100 | 3.5 hours | 75% (105/130) |

### Content Coverage

**Part 1: Individual Tax**
- Filing requirements, status, and exemptions
- Income inclusions and exclusions
- Deductions and credits
- Capital gains and losses
- Retirement plans and distributions
- Self-employment tax
- Alternative Minimum Tax

**Part 2: Business Tax**
- Business income and expenses
- Depreciation and Section 179
- Entity taxation (C-Corp, S-Corp, Partnership)
- Payroll taxes and employment issues
- Multi-state tax issues
- Accounting methods and periods

**Part 3: Ethics & Procedures**
- Treasury Circular 230 regulations
- Professional standards and ethics
- IRS practice rights and limitations
- Due diligence requirements
- Client confidentiality and conflicts of interest
- Disciplinary procedures and sanctions

## 🚀 Quick Start

### Prerequisites
- Node.js (v18 or higher)
- npm (Node Package Manager)
- Modern web browser

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ea-exam-practice.git
   cd ea-exam-practice
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the application**
   ```bash
   npm run dev
   ```

4. **Open in browser**
   Navigate to `http://localhost:5000` in your web browser

### Alternative: Python Launcher

Use the included Python launcher for a simplified start process:

```bash
python enrolled_agent_app.py
```

Available commands:
- `python enrolled_agent_app.py start` - Start the application (default)
- `python enrolled_agent_app.py install` - Install dependencies only
- `python enrolled_agent_app.py help` - Show help information

## 🛠️ Technology Stack

### Frontend
- **React 18**: Modern UI framework with hooks and functional components
- **TypeScript**: Type-safe development and better code quality
- **Tailwind CSS**: Utility-first CSS framework for responsive design
- **shadcn/ui**: Accessible component library built on Radix UI
- **React Query**: Server state management and caching
- **Wouter**: Lightweight client-side routing

### Backend
- **Node.js**: JavaScript runtime for server-side development
- **Express.js**: Fast, minimalist web framework
- **TypeScript**: Type-safe backend development
- **Drizzle ORM**: Type-safe database ORM
- **PostgreSQL**: Production database (optional, uses in-memory storage by default)

### Development Tools
- **Vite**: Fast build tool with hot module replacement
- **Drizzle Kit**: Database migrations and schema management
- **ESLint**: Code linting and quality enforcement
- **Prettier**: Code formatting and style consistency

## 📁 Project Structure

```
ea-exam-practice/
├── client/                 # Frontend React application
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── pages/          # Application pages/routes
│   │   ├── hooks/          # Custom React hooks
│   │   ├── lib/            # Utility functions and configurations
│   │   ├── types/          # TypeScript type definitions
│   │   └── data/           # Static data and question banks
├── server/                 # Backend Express application
│   ├── index.ts           # Server entry point
│   ├── routes.ts          # API route definitions
│   ├── storage.ts         # Data storage interface
│   └── vite.ts            # Vite development integration
├── shared/                # Shared type definitions
│   └── schema.ts          # Database schema and types
├── enrolled_agent_app.py  # Python launcher script
├── package.json           # Node.js dependencies and scripts
└── README.md             # This file
```

## 🎓 Study Guidance

### Recommended Study Plan
1. **Complete a formal EA course** (150-300 hours recommended)
2. **Review current tax law updates** for tax years 2021-2023
3. **Practice with this application** using both modes extensively
4. **Focus on weak areas** identified through practice tests
5. **Final review** of Circular 230 and IRS procedures

### Study Materials
- IRS Publication 17 (Your Federal Income Tax)
- Instructions for Forms 1040, 1120, 1120S, 1065
- Treasury Circular 230
- IRS continuing education materials
- This practice application

### Time Management Tips
- **Individual Tax**: ~2.1 minutes per question
- **Business Tax**: ~2.1 minutes per question
- **Ethics**: ~2.1 minutes per question
- Leave time for reviewing flagged questions

## 📊 Export Features

The application provides comprehensive export functionality:

### Practice Mode Export
- Flagged questions with full text and explanations
- Incorrect answers with detailed feedback
- Performance statistics by category
- Study recommendations based on weak areas

### Simulation Exam Export
- Complete session data with timing information
- Part-by-part performance breakdown
- Flagged questions across all exam parts
- Overall progress and completion status

Export files are generated in JSON format for easy review and offline study.

## 🏥 Official Exam Information

### Testing Conditions
- **Location**: Authorized Prometric test centers nationwide
- **Scheduling**: Appointments required (online or phone)
- **Identification**: Valid government-issued photo ID required
- **Materials**: No personal materials allowed; calculator provided
- **Breaks**: Optional 15-minute break between parts

### Scoring
- **Method**: Computer-scored immediately after completion
- **Passing Score**: 105 out of 130 questions correct per part
- **Partial Credit**: No partial credit; each question worth one point
- **Results**: Immediate preliminary results, official notice mailed within 6 weeks

### Post-Exam Requirements
- **Application**: Form 23 (Application for Enrollment to Practice)
- **Background Check**: IRS reviews tax compliance and conduct
- **Enrollment**: Treasury card issued upon approval
- **Continuing Education**: 72 hours every 3 years
- **Renewal**: Must renew enrollment every 3 years

## 🤝 Contributing

We welcome contributions to improve the EA Exam Practice Application! Please feel free to:

- Report bugs or issues
- Suggest new features
- Submit pull requests
- Improve documentation
- Add more practice questions

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/ea-exam-practice/issues) page for existing solutions
2. Create a new issue with detailed information about your problem
3. Include your operating system, Node.js version, and browser information

## 🎯 About the EA Exam

The Special Enrollment Examination (SEE) is administered by the IRS to determine who may represent taxpayers before the Internal Revenue Service. Enrolled Agents are federally licensed tax practitioners with unlimited rights to represent taxpayers before the IRS.

### Key Benefits of EA Certification
- Unlimited representation rights before the IRS
- National recognition and credibility
- Continuing education requirements ensure current knowledge
- No geographic restrictions on practice
- Valuable credential for tax professionals

---

**Good luck with your EA exam preparation!** 🍀

*This application is designed to supplement, not replace, comprehensive EA exam preparation courses and official study materials.*
