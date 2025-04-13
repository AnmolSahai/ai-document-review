import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'
import { resolve } from 'path'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: '../api/www',
    chunkSizeWarningLimit: 1000, // Increase warning limit to 1000kb
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom', 'react-router-dom'],
          ui: ['@fluentui/react-components', '@fluentui/react-icons'],
          pdf: ['react-pdf', 'annotpdf']
        }
      }
    }
  },
  server: {
    host: '127.0.0.1',
    proxy: {
      '/api': 'http://localhost:8000'
    }
  }
})
