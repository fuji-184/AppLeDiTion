import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import { viteStaticCopy } from 'vite-plugin-static-copy'

export default defineConfig({
	plugins: [
		sveltekit(),
		viteStaticCopy({
			targets: [
			  { src: 'node_modules/tinymce/*', dest: 'tinymce' }
			]
		  }),
	],
	server: {
		host: '127.0.0.1',
		port: 5173
	  }
});
