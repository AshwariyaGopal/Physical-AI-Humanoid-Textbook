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
    link: '/docs/Module-1-The-Robotic-Nervous-System-ROS-2/week-1-ros2-core-concepts',
  },
  {
    title: 'Simulation & Digital Twins',
    description: 'Dive into high-fidelity robotic simulation and the creation of digital twins. Understand how to model complex environments, integrate sensors, and test algorithms efficiently in virtual worlds before deployment.',
    link: '/docs/Module-2-The-Digital-Twin-Gazebo-Unity/week-3-physics-sensors',
  },
  {
    title: 'Isaac ROS and Hardware-Accelerated Visual SLAM (VSLAM)',
    description: 'Leverage NVIDIA\'s Isaac ROS platform to implement hardware-accelerated visual Simultaneous Localization and Mapping (VSLAM). Develop advanced perception pipelines for robots to navigate and understand their surroundings in real-time.',
    link: '/docs/Module-3-The-AI-Robot-Brain-NVIDIA-Isaac/week-4-perception-pipeline',
  },
  {
    title: 'Vision-Language-Action (VLA)',
    description: 'Explore the integration of visual perception, natural language understanding, and robotic action. Learn how to develop systems that allow robots to comprehend and execute complex instructions from human language.',
    link: '/docs/Module-4-Vision-Language-Action/week-5-llm-cognitive-planning',
  },
  {
    title: 'Control Theory for Humanoids',
    description: 'Delve into advanced control strategies for stable and agile humanoid robot motion. Cover topics such as whole-body control, balance, locomotion, and compliant interaction for safe and effective operation.',
    link: '/docs/Module-5-Control-Theory-for-Humanoids/week-6-stability-wbc',
  },
  {
    title: 'Ethical and Legal Embodiment (ELSI)',
    description: 'Examine the critical ethical, legal, and societal implications of intelligent humanoid robotics. Understand frameworks for responsible development, privacy, safety, and the societal impact of autonomous systems.',
    link: '/docs/Module-6-Ethical-and-Legal-Embodiment-ELSI/week-8-ethical-frameworks',
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

export default function ModuleCards(): React.ReactElement {
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
