import { Avatar, Button, Flex, Heading, IconButton, Text } from '@chakra-ui/react'

import profileUser from '../../assets/profile-user.jpg'

export function StudioHeader() {
  return (
    <Flex
      as="header"
      position="sticky"
      top={0}
      zIndex={40}
      px={{ base: 4, md: 6 }}
      py={4}
      align="center"
      justify="space-between"
      bg="rgba(12,14,17,0.86)"
      backdropFilter="blur(10px)"
      borderBottom="1px solid"
      borderColor="studio.border"
    >
      <Flex align="center" gap={{ base: 3, md: 8 }}>
        <Heading
          as="h1"
          size="lg"
          fontFamily="heading"
          fontWeight="900"
          letterSpacing="tight"
          color="studio.primary"
        >
          VocalSync Studio
        </Heading>
        <Flex display={{ base: 'none', md: 'flex' }} gap={6}>
          <Text fontFamily="heading" color="studio.primary" fontWeight="bold">
            Studio
          </Text>
          <Text color="studio.muted">Projects</Text>
          <Text color="studio.muted">Assets</Text>
        </Flex>
      </Flex>

      <Flex align="center" gap={2}>
        <Button
          size="sm"
          display={{ base: 'none', md: 'inline-flex' }}
          bg="studio.primaryStrong"
          color="studio.text"
          _hover={{ bg: 'studio.primaryHover' }}
        >
          + Create
        </Button>
        <IconButton aria-label="Settings" variant="ghost" color="studio.muted">
          ⚙
        </IconButton>
        <IconButton aria-label="Notifications" variant="ghost" color="studio.muted">
          🔔
        </IconButton>
        <Avatar.Root size="sm">
          <Avatar.Image src={profileUser} alt="User profile" />
          <Avatar.Fallback name="MP" />
        </Avatar.Root>
      </Flex>
    </Flex>
  )
}
