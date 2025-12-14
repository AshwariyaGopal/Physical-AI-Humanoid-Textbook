import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type ModuleItem = {
  title: string;
  description: string;
  link: string;
};

const ModuleList: ModuleItem[] = [
  {
    title: 'ROS 2 Foundations',
    description: 'Master the fundamentals of the Robot Operating System 2 (ROS 2), the essential framework for robotic application development. Learn core concepts like nodes, topics, services, and actions to build robust and scalable robot systems.',
    link: '/docs/01-ros2-fundamentals/01_core_concepts',
  },
  {
    title: 'Simulation & Digital Twins',
    description: 'Dive into high-fidelity robotic simulation and the creation of digital twins. Understand how to model complex environments, integrate sensors, and test algorithms efficiently in virtual worlds before deployment.',
    link: '/docs/02-digital-twin/01_physics_sensors',
  },
  {
    title: 'Isaac ROS and Hardware-Accelerated Visual SLAM (VSLAM)',
    description: 'Leverage NVIDIA\'s Isaac ROS platform to implement hardware-accelerated visual Simultaneous Localization and Mapping (VSLAM). Develop advanced perception pipelines for robots to navigate and understand their surroundings in real-time.',
    link: '/docs/03-isaac-platform/01_perception_pipeline',
  },
  {
    title: 'Vision-Language-Action (VLA)',
    description: 'Explore the integration of visual perception, natural language understanding, and robotic action. Learn how to develop systems that allow robots to comprehend and execute complex instructions from human language.',
    link: '/docs/04-vla/01_llm_cognitive_planning',
  },
  {
    title: 'Control Theory for Humanoids',
    description: 'Delve into advanced control strategies for stable and agile humanoid robot motion. Cover topics such as whole-body control, balance, locomotion, and compliant interaction for safe and effective operation.',
    link: '/docs/Control Theory for Humanoids/01_stability_wbc',
  },
  {
    title: 'Ethical and Legal Embodiment (ELSI)',
    description: 'Examine the critical ethical, legal, and societal implications of intelligent humanoid robotics. Understand frameworks for responsible development, privacy, safety, and the societal impact of autonomous systems.',
    link: '/docs/Ethical and Legal Embodiment (ELSI)/01_ethical_frameworks',
  },
  {
    title: 'Appendix',
    description: 'Access supplementary materials, advanced topics, and reference guides to deepen your understanding and extend your knowledge of Physical AI and Humanoid Robotics.',
    link: '/docs/appendix', // Assuming an appendix page exists or will be created
  },
];

function Module({ title, description, link }: ModuleItem) {
  return (
    <div className={clsx('col col--4', styles.moduleCard)}>
      <div className="card">
        <div className="card__header">
          <Heading as="h3">{title}</Heading>
        </div>
        <div className="card__body">
          <p>{description}</p>
        </div>
        <div className="card__footer">
          <Link
            className="button button--primary button--block"
            to={link}>
            {title === 'Appendix' ? 'Open Appendix →' : 'Open Module →'}
          </Link>
        </div>
      </div>
    </div>
  );
}

export default function ModuleCards(): JSX.Element {
  return (
    <section className={styles.modules}>
      <div className="container">
        <div className="row">
          <div className="col col--12 text--center margin-bottom--lg">
            <Heading as="h2">Explore All Modules</Heading>
          </div>
        </div>
        <div className="row">
          {ModuleList.map((props, idx) => (
            <Module key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
