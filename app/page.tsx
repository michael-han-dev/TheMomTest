import Link from 'next/link'
import Header from './components/Header'
import Footer from './components/Footer'

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />

      {/* Hero Section */}
      <section className="py-16 bg-gradient-to-r from-primary-50 to-secondary-50">
        <div className="container px-4 mx-auto">
          <div className="flex flex-col items-center md:flex-row">
            <div className="w-full md:w-1/2 md:pr-12">
              <h1 className="mb-6 text-4xl font-bold leading-tight text-gray-900 md:text-5xl">
                Validate Your Startup Idea The Right Way
              </h1>
              <p className="mb-8 text-lg text-gray-700">
                Stop wasting time on bad ideas. Use principles from "The Mom Test" to get honest feedback and validate your startup idea with confidence.
              </p>
              <div className="flex flex-col space-y-4 sm:flex-row sm:space-y-0 sm:space-x-4">
                <Link href="/validate" className="btn btn-primary">Start Validating</Link>
                <Link href="/learn" className="btn btn-outline">Learn More</Link>
              </div>
            </div>
            <div className="w-full mt-12 md:w-1/2 md:mt-0">
              <div className="relative h-64 overflow-hidden rounded-lg shadow-xl md:h-96">
                <div className="absolute inset-0 bg-gradient-to-r from-primary-500 to-secondary-500 opacity-20"></div>
                <div className="absolute inset-0 flex items-center justify-center">
                  <div className="p-8 text-center bg-white rounded-lg shadow-lg">
                    <h3 className="mb-4 text-xl font-bold">The Mom Test</h3>
                    <p className="text-gray-700">
                      "Talk about their life, not your idea. Ask about specifics in the past, not generics or opinions about the future."
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 bg-white">
        <div className="container px-4 mx-auto">
          <h2 className="mb-12 text-3xl font-bold text-center">How It Works</h2>
          <div className="grid grid-cols-1 gap-8 md:grid-cols-3">
            <div className="p-6 transition-all duration-300 bg-white rounded-lg shadow-md hover:shadow-lg">
              <div className="flex items-center justify-center w-12 h-12 mb-4 text-white bg-primary-500 rounded-full">1</div>
              <h3 className="mb-3 text-xl font-semibold">Define Your Idea</h3>
              <p className="text-gray-600">
                Clearly articulate your startup idea, target market, and the problem you're solving.
              </p>
            </div>
            <div className="p-6 transition-all duration-300 bg-white rounded-lg shadow-md hover:shadow-lg">
              <div className="flex items-center justify-center w-12 h-12 mb-4 text-white bg-primary-500 rounded-full">2</div>
              <h3 className="mb-3 text-xl font-semibold">Generate Interview Questions</h3>
              <p className="text-gray-600">
                Get AI-generated questions based on "The Mom Test" principles to avoid biased feedback.
              </p>
            </div>
            <div className="p-6 transition-all duration-300 bg-white rounded-lg shadow-md hover:shadow-lg">
              <div className="flex items-center justify-center w-12 h-12 mb-4 text-white bg-primary-500 rounded-full">3</div>
              <h3 className="mb-3 text-xl font-semibold">Analyze & Iterate</h3>
              <p className="text-gray-600">
                Record interview results, get AI analysis, and refine your idea based on real feedback.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-16 bg-primary-50">
        <div className="container px-4 mx-auto text-center">
          <h2 className="mb-4 text-3xl font-bold">Ready to Validate Your Idea?</h2>
          <p className="max-w-2xl mx-auto mb-8 text-lg text-gray-700">
            Join hundreds of founders who have saved time and money by validating their ideas properly.
          </p>
          <Link href="/signup" className="btn btn-primary">Get Started for Free</Link>
        </div>
      </section>

      <Footer />
    </div>
  )
} 