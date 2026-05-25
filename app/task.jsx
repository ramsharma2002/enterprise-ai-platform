'use client'

import { useState } from 'react'

export default function EnterpriseAIPlatformPreview() {
  const [activeTab, setActiveTab] = useState('overview')

  const stats = [
    { title: 'Active Teams', value: '124' },
    { title: 'Tasks Completed', value: '18.2K' },
    { title: 'Realtime Users', value: '2,431' },
    { title: 'AI Suggestions', value: '9.4K' },
  ]

  const tasks = [
    {
      title: 'Realtime Socket Optimization',
      priority: 'High',
      progress: '82%',
    },
    {
      title: 'AI Deadline Prediction Engine',
      priority: 'Medium',
      progress: '61%',
    },
    {
      title: 'Enterprise Analytics Dashboard',
      priority: 'High',
      progress: '94%',
    },
  ]

  return (
    <div className="min-h-screen bg-black text-white overflow-hidden">
      <div className="max-w-7xl mx-auto px-6 py-10">
        <div className="mb-12">
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-zinc-700 bg-zinc-900 mb-6">
            <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse" />
            <span className="text-sm text-zinc-300">
              Enterprise SaaS Platform Preview
            </span>
          </div>

          <h1 className="text-6xl md:text-7xl font-black leading-tight max-w-5xl bg-gradient-to-r from-white via-zinc-300 to-zinc-600 bg-clip-text text-transparent">
            AI-Powered Collaborative Productivity System
          </h1>

          <p className="text-zinc-400 text-lg mt-6 max-w-3xl leading-relaxed">
            A scalable enterprise collaboration ecosystem featuring realtime synchronization, intelligent workflow automation, modern analytics, and immersive user experiences.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-4 gap-5 mb-12">
          {stats.map((item, index) => (
            <div
              key={index}
              className="bg-zinc-900 border border-zinc-800 rounded-3xl p-6"
            >
              <p className="text-zinc-400 text-sm">{item.title}</p>
              <h2 className="text-4xl font-black mt-3">{item.value}</h2>
            </div>
          ))}
        </div>

        <div className="flex flex-wrap gap-4 mb-8">
          {['overview', 'tasks', 'ai', 'analytics'].map((tab) => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`px-5 py-3 rounded-2xl font-semibold transition ${
                activeTab === tab
                  ? 'bg-white text-black'
                  : 'bg-zinc-900 border border-zinc-800 text-zinc-300'
              }`}
            >
              {tab.charAt(0).toUpperCase() + tab.slice(1)}
            </button>
          ))}
        </div>

        {activeTab === 'overview' && (
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="lg:col-span-2 bg-zinc-900 border border-zinc-800 rounded-3xl p-8">
              <h2 className="text-3xl font-bold mb-6">
                Platform Architecture
              </h2>

              <div className="space-y-4 text-zinc-300">
                <div className="bg-zinc-800 rounded-2xl p-5">
                  Frontend → Next.js + Tailwind + Framer Motion
                </div>

                <div className="bg-zinc-800 rounded-2xl p-5">
                  Backend → Node.js + Express + Socket.io
                </div>

                <div className="bg-zinc-800 rounded-2xl p-5">
                  Database → PostgreSQL + Redis Cache Layer
                </div>

                <div className="bg-zinc-800 rounded-2xl p-5">
                  AI Engine → OpenAI + NLP Recommendation System
                </div>
              </div>
            </div>

            <div className="bg-zinc-900 border border-zinc-800 rounded-3xl p-8">
              <h2 className="text-3xl font-bold mb-6">
                System Health
              </h2>

              <div className="space-y-5">
                {[
                  ['API Uptime', '99.99%'],
                  ['Socket Latency', '280ms'],
                  ['AI Response Time', '1.2s'],
                  ['Database Load', 'Normal'],
                ].map(([label, value], index) => (
                  <div
                    key={index}
                    className="flex justify-between bg-zinc-800 rounded-2xl p-4"
                  >
                    <span className="text-zinc-400">{label}</span>
                    <span className="font-semibold">{value}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {activeTab === 'tasks' && (
          <div className="bg-zinc-900 border border-zinc-800 rounded-3xl p-8">
            <h2 className="text-3xl font-bold mb-8">Realtime Task Workspace</h2>

            <div className="space-y-5">
              {tasks.map((task, index) => (
                <div
                  key={index}
                  className="bg-zinc-800 rounded-3xl p-6"
                >
                  <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-5">
                    <div>
                      <h3 className="text-2xl font-bold">{task.title}</h3>
                      <p className="text-zinc-400 mt-1">
                        AI Priority: {task.priority}
                      </p>
                    </div>

                    <div className="px-4 py-2 rounded-full bg-green-500/20 text-green-300">
                      {task.progress}
                    </div>
                  </div>

                  <div className="h-4 bg-zinc-700 rounded-full overflow-hidden">
                    <div
                      style={{ width: task.progress }}
                      className="h-full bg-white"
                    />
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {activeTab === 'ai' && (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="bg-zinc-900 border border-zinc-800 rounded-3xl p-8">
              <h2 className="text-3xl font-bold mb-6">AI Insights</h2>

              <div className="space-y-4">
                <div className="bg-zinc-800 rounded-2xl p-5">
                  Productivity increased by 18% after workflow automation.
                </div>

                <div className="bg-zinc-800 rounded-2xl p-5">
                  Backend optimization tasks are predicted to become overdue in 48 hours.
                </div>

                <div className="bg-zinc-800 rounded-2xl p-5">
                  Team workload imbalance detected across engineering squads.
                </div>
              </div>
            </div>

            <div className="bg-zinc-900 border border-zinc-800 rounded-3xl p-8">
              <h2 className="text-3xl font-bold mb-6">AI Workflow Pipeline</h2>

              <div className="space-y-4 text-zinc-300">
                {[
                  'Task Submission',
                  'NLP Categorization',
                  'Priority Scoring',
                  'Deadline Forecasting',
                  'Recommendation Generation',
                  'Realtime Dashboard Sync',
                ].map((step, index) => (
                  <div
                    key={index}
                    className="bg-zinc-800 rounded-2xl p-4"
                  >
                    {index + 1}. {step}
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {activeTab === 'analytics' && (
          <div className="bg-zinc-900 border border-zinc-800 rounded-3xl p-8">
            <h2 className="text-4xl font-black mb-8">
              Enterprise Analytics Dashboard
            </h2>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {[
                ['Completion Rate', '94%'],
                ['AI Efficiency Gain', '+18%'],
                ['Average API Time', '118ms'],
              ].map(([title, value], index) => (
                <div
                  key={index}
                  className="bg-zinc-800 rounded-3xl p-6"
                >
                  <p className="text-zinc-400 mb-3">{title}</p>
                  <h2 className="text-5xl font-black">{value}</h2>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
