# Enterprise AI Platform

A modern, interactive AI-powered collaborative productivity system built with **Next.js**, **React**, and **Tailwind CSS**.

## Features

- 📊 **Real-time Dashboard** - Live stats and metrics tracking
- 🤖 **AI-Powered Insights** - Intelligent workflow recommendations
- 📈 **Enterprise Analytics** - Comprehensive performance monitoring
- ⚡ **Task Tracking** - Real-time task management with progress tracking
- 🎨 **Modern UI** - Sleek dark theme with gradient accents
- 📱 **Responsive Design** - Works seamlessly on all devices

## Tech Stack

- **Frontend**: Next.js 14, React 18, Tailwind CSS
- **Styling**: Tailwind CSS with custom configurations
- **State Management**: React Hooks (useState)
- **Build Tool**: Next.js with SWC compiler

## Getting Started

### Prerequisites
- Node.js 18+ (https://nodejs.org)
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Task
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser to view the application.

## Project Structure

```
app/
├── layout.jsx          # Root layout with metadata
├── page.jsx            # Home page (entry point)
├── task.jsx            # Main Enterprise AI Platform component
├── globals.css         # Global styles
└── node_modules/       # Dependencies

Configuration Files:
├── next.config.js      # Next.js configuration
├── tailwind.config.js  # Tailwind CSS configuration
├── postcss.config.js   # PostCSS configuration
├── package.json        # Project dependencies
└── tsconfig.json       # TypeScript configuration
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm start` - Start production server
- `npm run lint` - Run ESLint

## Features in Detail

### Dashboard Stats
- Active Teams: 124
- Tasks Completed: 18.2K
- Realtime Users: 2,431
- AI Suggestions: 9.4K

### Tab Navigation
- **Overview** - Platform architecture and system health
- **Tasks** - Real-time task workspace with progress tracking
- **AI** - AI insights and workflow pipeline
- **Analytics** - Enterprise analytics dashboard

## Customization

### Adding New Stats
Edit `task.jsx` stats array to add or modify metrics:
```javascript
const stats = [
  { title: 'Your Metric', value: 'XXX' },
  // ...
]
```

### Theming
Customize colors in `tailwind.config.js` or modify utility classes directly in component classNames.

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Performance

- ⚡ Fast page loads with Next.js optimization
- 🎯 Efficient component rendering with React
- 🎨 Lightweight CSS with Tailwind
- 📦 Optimized bundle size

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use this project for any purpose.

## Contact

For questions or feedback, please open an issue on GitHub.

---

**Built with ❤️ using Next.js and React**
