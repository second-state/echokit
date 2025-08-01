import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Full stack open-source',
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        Firmware, AI agents, MCP servers, AI/LLM model inference, ESP 32 servers are all open sourced. Complete solution from embedded firmware to AI inference server.
      </>
    ),
  },
  {
    title: 'Customize your AI agent exprience',
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        Choose your preferred AI models including LLMs, voice to text, and TTS model, or switch between them seamlessly. You can also build your voice AI agent with MCP and agentic search.
      </>
    ),
  },
  {
    title: 'Designed for learning',
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        Learn AI from inside out by our full documentation and tutorials. You will master how to build and customize your own AI system on your own computers
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
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

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
