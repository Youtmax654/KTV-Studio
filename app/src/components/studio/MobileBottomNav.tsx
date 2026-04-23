import { Flex, Text } from '@chakra-ui/react'

export function MobileBottomNav() {
  return (
    <Flex
      as="nav"
      position="fixed"
      bottom={0}
      left={0}
      right={0}
      display={{ base: 'flex', md: 'none' }}
      justify="space-around"
      bg="rgba(12,14,17,0.95)"
      borderTop="1px solid"
      borderColor="studio.border"
      py={2}
    >
      <Text color="studio.primary">Home</Text>
      <Text color="studio.muted">Assistant</Text>
      <Text color="studio.muted">Editor</Text>
      <Text color="studio.muted">Account</Text>
    </Flex>
  )
}
