import { Badge, Box, Button, Card, Flex, Heading, Image, Text } from '@chakra-ui/react'

import type { Session } from './types'

type FeaturedSessionCardProps = {
  session: Session
}

export function FeaturedSessionCard({ session }: FeaturedSessionCardProps) {
  return (
    <Card.Root
      overflow="hidden"
      border="1px solid"
      borderColor="studio.border"
      minH={{ base: '300px', lg: '460px' }}
      bg="studio.panelAlt"
    >
      <Box position="relative" h="full">
        {session.image && (
          <Image
            src={session.image}
            alt={session.title}
            h="100%"
            w="100%"
            objectFit="cover"
            opacity={0.58}
          />
        )}
        <Box
          position="absolute"
          inset={0}
          bgGradient="linear(to-t, rgba(0,0,0,0.92), rgba(0,0,0,0.08))"
        />
        <Flex position="absolute" inset={0} direction="column" justify="flex-end" p={6}>
          <Flex gap={2} mb={3} wrap="wrap">
            <Badge bg="blackAlpha.500" color="studio.success" px={2} py={1} rounded="full">
              {session.status}
            </Badge>
            <Badge bg="blackAlpha.400" color="studio.muted">
              {session.language}
            </Badge>
            <Badge bg="blackAlpha.400" color="studio.muted">
              {session.vibe}
            </Badge>
          </Flex>
          <Heading fontFamily="heading" size="2xl" mb={2}>
            {session.title}
          </Heading>
          <Text color="studio.muted" mb={5}>
            {session.updated}
          </Text>
          <Flex gap={2}>
            <Button bg="studio.primaryStrong" _hover={{ bg: 'studio.primaryHover' }} color="studio.text">
              Open Editor
            </Button>
            <Button variant="outline" borderColor="studio.subtle">
              Share
            </Button>
          </Flex>
        </Flex>
      </Box>
    </Card.Root>
  )
}
