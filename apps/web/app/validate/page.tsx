'use client'

import { useState } from 'react'
import Header from '../components/Header'
import Footer from '../components/Footer'

export default function ValidatePage() {
  const [step, setStep] = useState(1)
  const [formData, setFormData] = useState({
    ideaName: '',
    problemStatement: '',
    targetAudience: '',
    solution: '',
    valueProposition: '',
  })

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target
    setFormData(prev => ({ ...prev, [name]: value }))
  }

  const handleNext = () => {
    setStep(prev => prev + 1)
  }

  const handleBack = () => {
    setStep(prev => prev - 1)
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // Here you would typically send the data to your backend
    console.log('Form submitted:', formData)
    // Move to the next step (results page)
    setStep(4)
  }

  return (
    <div className="flex flex-col min-h-screen">
      <Header />

      <main className="flex-grow py-12 bg-gray-50">
        <div className="container px-4 mx-auto">
          <div className="max-w-3xl mx-auto">
            <div className="mb-8">
              <h1 className="mb-4 text-3xl font-bold text-gray-900">Validate Your Startup Idea</h1>
              <p className="text-lg text-gray-700">
                Follow the steps below to start validating your startup idea using principles from "The Mom Test".
              </p>
            </div>

            {/* Progress Steps */}
            <div className="mb-8">
              <div className="flex items-center justify-between">
                <div className={`flex flex-col items-center ${step >= 1 ? 'text-primary-600' : 'text-gray-400'}`}>
                  <div className={`flex items-center justify-center w-10 h-10 mb-2 rounded-full ${step >= 1 ? 'bg-primary-600 text-white' : 'bg-gray-200 text-gray-500'}`}>
                    1
                  </div>
                  <span className="text-sm font-medium">Define Idea</span>
                </div>
                <div className={`flex-1 h-1 mx-4 ${step >= 2 ? 'bg-primary-500' : 'bg-gray-200'}`}></div>
                <div className={`flex flex-col items-center ${step >= 2 ? 'text-primary-600' : 'text-gray-400'}`}>
                  <div className={`flex items-center justify-center w-10 h-10 mb-2 rounded-full ${step >= 2 ? 'bg-primary-600 text-white' : 'bg-gray-200 text-gray-500'}`}>
                    2
                  </div>
                  <span className="text-sm font-medium">Target Audience</span>
                </div>
                <div className={`flex-1 h-1 mx-4 ${step >= 3 ? 'bg-primary-500' : 'bg-gray-200'}`}></div>
                <div className={`flex flex-col items-center ${step >= 3 ? 'text-primary-600' : 'text-gray-400'}`}>
                  <div className={`flex items-center justify-center w-10 h-10 mb-2 rounded-full ${step >= 3 ? 'bg-primary-600 text-white' : 'bg-gray-200 text-gray-500'}`}>
                    3
                  </div>
                  <span className="text-sm font-medium">Solution</span>
                </div>
                <div className={`flex-1 h-1 mx-4 ${step >= 4 ? 'bg-primary-500' : 'bg-gray-200'}`}></div>
                <div className={`flex flex-col items-center ${step >= 4 ? 'text-primary-600' : 'text-gray-400'}`}>
                  <div className={`flex items-center justify-center w-10 h-10 mb-2 rounded-full ${step >= 4 ? 'bg-primary-600 text-white' : 'bg-gray-200 text-gray-500'}`}>
                    4
                  </div>
                  <span className="text-sm font-medium">Results</span>
                </div>
              </div>
            </div>

            {/* Form Steps */}
            <div className="p-8 bg-white rounded-lg shadow-md">
              {step === 1 && (
                <div>
                  <h2 className="mb-6 text-2xl font-semibold">Define Your Idea</h2>
                  <div className="mb-6">
                    <label htmlFor="ideaName" className="block mb-2 text-sm font-medium text-gray-700">
                      Idea Name
                    </label>
                    <input
                      type="text"
                      id="ideaName"
                      name="ideaName"
                      value={formData.ideaName}
                      onChange={handleChange}
                      className="input"
                      placeholder="Name your idea"
                      required
                    />
                  </div>
                  <div className="mb-6">
                    <label htmlFor="problemStatement" className="block mb-2 text-sm font-medium text-gray-700">
                      Problem Statement
                    </label>
                    <textarea
                      id="problemStatement"
                      name="problemStatement"
                      value={formData.problemStatement}
                      onChange={handleChange}
                      rows={4}
                      className="input"
                      placeholder="Describe the problem your idea solves"
                      required
                    ></textarea>
                  </div>
                  <div className="flex justify-end">
                    <button
                      type="button"
                      onClick={handleNext}
                      className="btn btn-primary"
                    >
                      Next
                    </button>
                  </div>
                </div>
              )}

              {step === 2 && (
                <div>
                  <h2 className="mb-6 text-2xl font-semibold">Define Your Target Audience</h2>
                  <div className="mb-6">
                    <label htmlFor="targetAudience" className="block mb-2 text-sm font-medium text-gray-700">
                      Target Audience
                    </label>
                    <textarea
                      id="targetAudience"
                      name="targetAudience"
                      value={formData.targetAudience}
                      onChange={handleChange}
                      rows={4}
                      className="input"
                      placeholder="Describe your target audience"
                      required
                    ></textarea>
                  </div>
                  <div className="flex justify-between">
                    <button
                      type="button"
                      onClick={handleBack}
                      className="btn btn-outline"
                    >
                      Back
                    </button>
                    <button
                      type="button"
                      onClick={handleNext}
                      className="btn btn-primary"
                    >
                      Next
                    </button>
                  </div>
                </div>
              )}

              {step === 3 && (
                <form onSubmit={handleSubmit}>
                  <h2 className="mb-6 text-2xl font-semibold">Define Your Solution</h2>
                  <div className="mb-6">
                    <label htmlFor="solution" className="block mb-2 text-sm font-medium text-gray-700">
                      Solution Description
                    </label>
                    <textarea
                      id="solution"
                      name="solution"
                      value={formData.solution}
                      onChange={handleChange}
                      rows={4}
                      className="input"
                      placeholder="Describe your solution"
                      required
                    ></textarea>
                  </div>
                  <div className="mb-6">
                    <label htmlFor="valueProposition" className="block mb-2 text-sm font-medium text-gray-700">
                      Value Proposition
                    </label>
                    <textarea
                      id="valueProposition"
                      name="valueProposition"
                      value={formData.valueProposition}
                      onChange={handleChange}
                      rows={4}
                      className="input"
                      placeholder="What unique value does your solution provide?"
                      required
                    ></textarea>
                  </div>
                  <div className="flex justify-between">
                    <button
                      type="button"
                      onClick={handleBack}
                      className="btn btn-outline"
                    >
                      Back
                    </button>
                    <button
                      type="submit"
                      className="btn btn-primary"
                    >
                      Generate Validation Plan
                    </button>
                  </div>
                </form>
              )}

              {step === 4 && (
                <div>
                  <h2 className="mb-6 text-2xl font-semibold">Your Validation Plan</h2>
                  
                  <div className="p-6 mb-6 bg-primary-50 rounded-lg">
                    <h3 className="mb-4 text-xl font-semibold text-primary-700">Interview Questions</h3>
                    <p className="mb-4 text-gray-700">
                      Based on your idea, here are some questions you should ask potential customers:
                    </p>
                    <ul className="pl-5 mb-4 space-y-2 list-disc">
                      <li>What's the hardest part about [problem area] in your day-to-day work?</li>
                      <li>Can you walk me through the last time you encountered this problem?</li>
                      <li>What solutions have you tried before? What worked and what didn't?</li>
                      <li>How much time/money do you currently spend dealing with this issue?</li>
                      <li>How are you currently solving this problem?</li>
                    </ul>
                    <div className="p-4 bg-yellow-50 border-l-4 border-yellow-400">
                      <p className="text-sm text-yellow-700">
                        <strong>Remember:</strong> Don't ask leading questions or pitch your idea. Focus on their problems, not your solution.
                      </p>
                    </div>
                  </div>

                  <div className="p-6 mb-6 bg-gray-50 rounded-lg">
                    <h3 className="mb-4 text-xl font-semibold">Market Research Insights</h3>
                    <p className="mb-2 text-gray-700">
                      To validate your idea further, we recommend researching these platforms:
                    </p>
                    <ul className="pl-5 mb-4 space-y-1 list-disc">
                      <li>Reddit communities related to your industry</li>
                      <li>Twitter: Follow industry experts and potential customers</li>
                      <li>Product Hunt: Check similar products and their reviews</li>
                      <li>Industry forums and communities</li>
                    </ul>
                  </div>

                  <div className="p-6 mb-6 bg-green-50 rounded-lg">
                    <h3 className="mb-4 text-xl font-semibold text-green-700">Next Steps</h3>
                    <ol className="pl-5 space-y-2 list-decimal">
                      <li>Conduct customer interviews using the questions above</li>
                      <li>Record and analyze the responses</li>
                      <li>Identify patterns and pain points</li>
                      <li>Return to this platform to analyze your findings</li>
                    </ol>
                  </div>

                  <div className="flex justify-between">
                    <button
                      type="button"
                      onClick={() => setStep(1)}
                      className="btn btn-outline"
                    >
                      Start Over
                    </button>
                    <button
                      type="button"
                      className="btn btn-primary"
                      onClick={() => window.print()}
                    >
                      Save Plan
                    </button>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </main>

      <Footer />
    </div>
  )
} 