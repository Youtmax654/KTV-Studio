import { Button, Card, Flex, Heading, Input, Text } from '@chakra-ui/react'

export function HeroSection() {
  return (
    <Card.Root
      bg="linear-gradient(155deg, rgba(151,169,255,0.13) 0%, rgba(23,26,29,1) 45%)"
      border="1px solid"
      borderColor="rgba(113,139,255,0.22)"
      rounded="2xl"
      mb={10}
    >
      <Card.Body py={{ base: 10, md: 14 }} px={{ base: 5, md: 12 }} textAlign="center">
        <Heading fontFamily="heading" fontWeight="800" fontSize={{ base: '3xl', md: '5xl' }} mb={3}>
          Start the Pulse
        </Heading>
        <Text color="studio.muted" maxW="720px" mx="auto" mb={8}>
          Drop a link or search our library to instantly generate karaoke timing,
          lyrics, and visuals.
        </Text>
        <Flex direction={{ base: 'column', md: 'row' }} gap={3} maxW="780px" mx="auto">
          <Flex
            flex={1}
            align="center"
            bg="studio.panel"
            border="1px solid"
            borderColor="studio.border"
            px={4}
            py={3}
            rounded="xl"
          >
            <Text color="studio.primary" mr={3}>
              🔗
            </Text>
            <Input
              placeholder="Paste YouTube link or type title..."
              border="none"
              _focusVisible={{ outline: 'none', boxShadow: 'none' }}
              px={0}
            />
          </Flex>
          <Button
            px={7}
            py={3}
            rounded="xl"
            bg="studio.primaryStrong"
            _hover={{ bg: 'studio.primary' }}
            color="studio.text"
            fontWeight="700"
          >
            Generate
          </Button>
        </Flex>
      </Card.Body>
    </Card.Root>
  )
}
