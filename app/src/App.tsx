import { Box } from '@chakra-ui/react'

import { HeroSection } from './components/studio/HeroSection'
import { MobileBottomNav } from './components/studio/MobileBottomNav'
import { RecentSessionsSection } from './components/studio/RecentSessionsSection'
import { sessions } from './components/studio/session-data'
import { StudioHeader } from './components/studio/StudioHeader'

function App() {
  return (
    <Box minH="100vh" bg="studio.bg" color="studio.text" pb={{ base: '80px', md: 0 }}>
      <StudioHeader />

      <Box maxW="1200px" mx="auto" px={{ base: 4, md: 8 }} pt={{ base: 5, md: 8 }}>
        <HeroSection />
        <RecentSessionsSection sessions={sessions} />
      </Box>

      <MobileBottomNav />
    </Box>
  )
}

export default App
