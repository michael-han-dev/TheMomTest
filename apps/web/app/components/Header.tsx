'use client'

import { useState } from 'react'
import Link from 'next/link'
import { usePathname } from 'next/navigation'

export default function Header() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)
  const pathname = usePathname()

  const isActive = (path: string) => {
    return pathname === path ? 'text-primary-600 font-medium' : 'text-gray-700 hover:text-primary-600'
  }

  return (
    <header className="sticky top-0 z-10 bg-white shadow-sm">
      <div className="container flex items-center justify-between px-4 py-4 mx-auto">
        <div className="flex items-center space-x-2">
          <Link href="/" className="text-xl font-bold text-primary-600">
            The Mom Test Bot
          </Link>
        </div>

        {/* Desktop Navigation */}
        <nav className="hidden space-x-6 md:flex">
          <Link href="/" className={isActive('/')}>
            Home
          </Link>
          <Link href="/about" className={isActive('/about')}>
            About
          </Link>
          <Link href="/features" className={isActive('/features')}>
            Features
          </Link>
          <Link href="/validate" className={isActive('/validate')}>
            Validate
          </Link>
        </nav>

        {/* Auth Buttons */}
        <div className="hidden items-center space-x-4 md:flex">
          <Link href="/login" className="btn btn-outline">
            Log in
          </Link>
          <Link href="/signup" className="btn btn-primary">
            Sign up
          </Link>
        </div>

        {/* Mobile Menu Button */}
        <button
          type="button"
          className="inline-flex items-center justify-center p-2 text-gray-400 rounded-md md:hidden hover:text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-primary-500"
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
        >
          <span className="sr-only">Open main menu</span>
          {mobileMenuOpen ? (
            <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          ) : (
            <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          )}
        </button>
      </div>

      {/* Mobile Menu */}
      {mobileMenuOpen && (
        <div className="md:hidden">
          <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3">
            <Link
              href="/"
              className={`block px-3 py-2 rounded-md ${isActive('/')}`}
              onClick={() => setMobileMenuOpen(false)}
            >
              Home
            </Link>
            <Link
              href="/about"
              className={`block px-3 py-2 rounded-md ${isActive('/about')}`}
              onClick={() => setMobileMenuOpen(false)}
            >
              About
            </Link>
            <Link
              href="/features"
              className={`block px-3 py-2 rounded-md ${isActive('/features')}`}
              onClick={() => setMobileMenuOpen(false)}
            >
              Features
            </Link>
            <Link
              href="/validate"
              className={`block px-3 py-2 rounded-md ${isActive('/validate')}`}
              onClick={() => setMobileMenuOpen(false)}
            >
              Validate
            </Link>
          </div>
          <div className="pt-4 pb-3 border-t border-gray-200">
            <div className="flex items-center px-5">
              <Link href="/login" className="block w-full px-5 py-3 text-center font-medium text-primary-600 bg-gray-50 hover:bg-gray-100">
                Log in
              </Link>
            </div>
            <div className="mt-3 px-5">
              <Link href="/signup" className="block w-full px-5 py-3 text-center font-medium text-white bg-primary-600 hover:bg-primary-700 rounded-md">
                Sign up
              </Link>
            </div>
          </div>
        </div>
      )}
    </header>
  )
} 