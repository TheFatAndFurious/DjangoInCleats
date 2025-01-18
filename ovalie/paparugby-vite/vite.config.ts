import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    outDir: '../static/news/assets', // Output directory for your Django static files
    emptyOutDir: true,
    manifest: true,
    rollupOptions: {
      input: './src/main.ts', // Specify your entry point(s)
    },
  },
  server: {
    watch: {
      usePolling: true,       // Necessary for some environments (e.g., Docker)
    },
    strictPort: true,          // Ensures the dev server uses the specified port
    port: 5173,               // Vite's default port
  },
});
