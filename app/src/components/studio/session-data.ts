import sessionBohemian from '../../assets/session-bohemian.jpg'
import sessionLevitating from '../../assets/session-levitating.jpg'
import sessionMidnight from '../../assets/session-midnight.jpg'
import sessionTiti from '../../assets/session-titi.jpg'
import type { Session } from './types'

export const sessions: Session[] = [
  {
    title: 'Midnight City - M83',
    status: 'Completed',
    language: 'EN',
    vibe: 'Duet',
    updated: 'Ready for final styling export',
    image: sessionMidnight,
    featured: true,
  },
  {
    title: 'Levitating - Dua Lipa',
    status: 'Draft',
    language: 'EN',
    vibe: 'Solo',
    updated: 'Edited 2h ago',
    image: sessionLevitating,
  },
  {
    title: 'Titi Me Pregunto',
    status: 'Exported',
    language: 'ES',
    vibe: 'Rap',
    updated: 'Edited yesterday',
    image: sessionTiti,
  },
  {
    title: 'Bohemian Rhapsody',
    status: 'Draft',
    language: 'EN',
    vibe: 'Group',
    updated: 'Edited 3 days ago',
    image: sessionBohemian,
  },
  {
    title: 'Blank Project',
    status: 'New',
    language: '-',
    vibe: '-',
    updated: 'Start from scratch',
  },
]
