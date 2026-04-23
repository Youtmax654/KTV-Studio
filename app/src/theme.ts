import { createSystem, defaultConfig } from '@chakra-ui/react'

export const system = createSystem(defaultConfig, {
  theme: {
    tokens: {
      fonts: {
        heading: { value: "'Space Grotesk', sans-serif" },
        body: { value: "'Manrope', sans-serif" },
      },
      colors: {
        studio: {
          bg: { value: '#0c0e11' },
          panel: { value: '#111417' },
          panelAlt: { value: '#171a1d' },
          border: { value: '#46484b' },
          text: { value: '#f9f9fd' },
          muted: { value: '#aaabaf' },
          subtle: { value: '#747579' },
          primary: { value: '#97a9ff' },
          primaryStrong: { value: '#3e65ff' },
          primaryHover: { value: '#5d7cff' },
          success: { value: '#ddffb0' },
          warning: { value: '#ff6f7c' },
        },
      },
    },
  },
})
