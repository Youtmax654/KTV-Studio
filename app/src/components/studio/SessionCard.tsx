import { Badge, Box, Card, Flex, Heading, Image, Text } from '@chakra-ui/react'

import type { Session } from './types'

type SessionCardProps = {
  session: Session
}

export function SessionCard({ session }: SessionCardProps) {
  return (
    <Card.Root bg="studio.panelAlt" border="1px solid" borderColor="studio.border" overflow="hidden">
      <Box h="132px" bg="studio.panel" position="relative">
        {session.image ? (
          <Image src={session.image} alt={session.title} h="100%" w="100%" objectFit="cover" opacity={0.56} />
        ) : (
          <Flex h="full" align="center" justify="center" fontSize="4xl" color="studio.subtle">
            +
          </Flex>
        )}
        <Badge
          position="absolute"
          left={3}
          top={3}
          bg="blackAlpha.600"
          color={session.status === 'Exported' ? 'studio.primary' : 'studio.warning'}
        >
          {session.status}
        </Badge>
      </Box>
      <Card.Body>
        <Heading fontFamily="heading" size="md" mb={1}>
          {session.title}
        </Heading>
        <Text color="studio.muted" fontSize="sm" mb={4}>
          {session.language} • {session.vibe}
        </Text>
        <Text color="studio.subtle" fontSize="xs">
          {session.updated}
        </Text>
      </Card.Body>
    </Card.Root>
  )
}
