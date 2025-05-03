import type { MetadataRoute } from "next";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "Next.js PWA",
    short_name: "NextPWA",
    description: "Tri-Aid Disaster Assessment Platform",
    start_url: "/",
    display: "standalone",
    background_color: "#ffffff",
    theme_color: "#000000",
    icons: [
      {
        src: "/icon-logo.png",
        sizes: "192x192",
        type: "image/png",
      },
      {
        src: "/icon-logo-2.png",
        sizes: "512x512",
        type: "image/png",
      },
    ],
  };
}
