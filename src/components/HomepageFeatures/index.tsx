import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Embodied AI',
    Svg: require('@site/static/img/EMBODIED_AI.jpeg').default,
    description: (
      <>
        Explore how intelligent systems learn to perceive and interact with the physical world. This section delves into the principles of embodied cognition and real-world robotic applications.
      </>
    ),
  },
  {
    title: 'Sim-to-Real Transfer',
    Svg: require('@site/static/img/SIM_AI.png').default,
    description: (
      <>
        Learn the techniques for developing and testing robot behaviors in high-fidelity simulations. Discover how to effectively transfer these learned skills to physical robots for robust performance.
      </>
    ),
  },
  {
    title: 'Vision-Language-Action',
    Svg: require('@site/static/img/VISION_AI.jpeg').default,
    description: (
      <>
        Understand the synergy of perception, language, and physical action in advanced robotic platforms. Build systems that interpret complex commands and execute intelligent tasks autonomously.
      </>
    ),
  },
];

function Feature({title, Svg, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          <div className="col col--12 text--center margin-bottom--lg">
            <Heading as="h1" className={clsx('hero__title', styles.learnHeading)}>What You Will Learn</Heading>
            <p className={clsx('hero__subtitle', styles.learnParagraph)}>Discover the engineering principles behind Physical AI as you learn to build, simulate, and control humanoid robots from the ground up. This curriculum guides you through essential technologies including ROS2, digital twins, and modern control theory, enabling you to translate code into real-world motion. By mastering these integrated systems, you will acquire the practical skills necessary to design and deploy autonomous machines capable of complex interaction.</p>
          </div>
        </div>
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
