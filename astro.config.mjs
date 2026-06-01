// @ts-check
import { defineConfig } from 'astro/config';

delete process.env.CF_PAGES;

import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://freelancer-tax-estimator.pages.dev',
  vite: {
    plugins: [tailwindcss()]
  },
  integrations: [sitemap()]
});
