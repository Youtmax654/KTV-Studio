import { Box, Flex, Grid, Heading, Link, SimpleGrid, Text } from '@chakra-ui/react'

import { FeaturedSessionCard } from './FeaturedSessionCard'
import { SessionCard } from './SessionCard'
import type { Session } from './types'

type RecentSessionsSectionProps = {
  sessions: Session[]
}

export function RecentSessionsSection({ sessions }: RecentSessionsSectionProps) {
  const featuredSessions = sessions.filter((session) => session.featured)
  const regularSessions = sessions.filter((session) => !session.featured)

  return (
    <>
      <Flex justify="space-between" align="end" mb={4} px={1}>
        <Box>
          <Heading fontFamily="heading" size="xl">
            Recent Sessions
          </Heading>
          <Text color="studio.muted" fontSize="sm" mt={1}>
            Jump back into your active edits
          </Text>
        </Box>
        <Link color="studio.primary" display={{ base: 'none', md: 'inline' }}>
          View Library {'->'}
        </Link>
      </Flex>

      <Grid templateColumns={{ base: '1fr', lg: '2fr 1fr 1fr' }} gap={5}>
        {featuredSessions.map((session) => (
          <FeaturedSessionCard key={session.title} session={session} />
        ))}

        <SimpleGrid columns={{ base: 1, md: 2, lg: 1 }} gap={5}>
          {regularSessions.map((session) => (
            <SessionCard key={session.title} session={session} />
          ))}
        </SimpleGrid>
      </Grid>
    </>
  )
}
