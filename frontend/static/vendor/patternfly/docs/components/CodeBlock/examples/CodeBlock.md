---
id: 'Code block'
section: components
cssPrefix: pf-v6-c-code-block
---## Examples

### Basic

```html
<div class="pf-v6-c-code-block">
  <div class="pf-v6-c-code-block__header">
    <div class="pf-v6-c-code-block__actions">
      <div class="pf-v6-c-code-block__actions-item">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Copy to clipboard basic example code content"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 448 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M320 448v40c0 13.255-10.745 24-24 24H24c-13.255 0-24-10.745-24-24V120c0-13.255 10.745-24 24-24h72v296c0 30.879 25.121 56 56 56h168zm0-344V0H152c-13.255 0-24 10.745-24 24v368c0 13.255 10.745 24 24 24h272c13.255 0 24-10.745 24-24V128H344c-13.2 0-24-10.8-24-24zm120.971-31.029L375.029 7.029A24 24 0 0 0 358.059 0H352v96h96v-6.059a24 24 0 0 0-7.029-16.97z"
              />
            </svg>
          </span>
        </button>
      </div>
      <div class="pf-v6-c-code-block__actions-item">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Run basic example code in Web Terminal"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 448 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M424.4 214.7L72.4 6.6C43.8-10.3 0 6.1 0 47.9V464c0 37.5 40.7 60.1 72.4 41.3l352-208c31.4-18.5 31.5-64.1 0-82.6z"
              />
            </svg>
          </span>
        </button>
      </div>
    </div>
  </div>
  <div class="pf-v6-c-code-block__content">
    <pre class="pf-v6-c-code-block__pre"><code class="pf-v6-c-code-block__code">apiVersion: helm.openshift.io/v1beta1/
kind: HelmChartRepository
metadata:
name: azure-sample-repo
spec:
connectionConfig:
url: https://raw.githubusercontent.com/Azure-Samples/helm-charts/master/docs</code>
</pre>
  </div>
</div>

```

### Expandable

```html
<div class="pf-v6-c-code-block">
  <div class="pf-v6-c-code-block__header">
    <div class="pf-v6-c-code-block__actions">
      <div class="pf-v6-c-code-block__actions-item">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Copy to clipboard expandable example code content"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 448 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M320 448v40c0 13.255-10.745 24-24 24H24c-13.255 0-24-10.745-24-24V120c0-13.255 10.745-24 24-24h72v296c0 30.879 25.121 56 56 56h168zm0-344V0H152c-13.255 0-24 10.745-24 24v368c0 13.255 10.745 24 24 24h272c13.255 0 24-10.745 24-24V128H344c-13.2 0-24-10.8-24-24zm120.971-31.029L375.029 7.029A24 24 0 0 0 358.059 0H352v96h96v-6.059a24 24 0 0 0-7.029-16.97z"
              />
            </svg>
          </span>
        </button>
      </div>
      <div class="pf-v6-c-code-block__actions-item">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Run expandable example code in Web Terminal"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 448 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M424.4 214.7L72.4 6.6C43.8-10.3 0 6.1 0 47.9V464c0 37.5 40.7 60.1 72.4 41.3l352-208c31.4-18.5 31.5-64.1 0-82.6z"
              />
            </svg>
          </span>
        </button>
      </div>
    </div>
  </div>
  <div class="pf-v6-c-code-block__content">
    <pre class="pf-v6-c-code-block__pre"><code class="pf-v6-c-code-block__code">apiVersion: helm.openshift.io/v1beta1/
kind: HelmChartRepository
metadata:
name: azure-sample-repo<div
  class="pf-v6-c-expandable-section pf-m-detached"
><div
  class="pf-v6-c-expandable-section__content"
  hidden
  id="code-block-expandable-content"
  role="region"
  aria-labelledby="code-block-expandable-toggle"
>
  spec:
  connectionConfig:
  url: https://raw.githubusercontent.com/Azure-Samples/helm-charts/master/docs</div>
</div>
</code>
</pre>
    <div class="pf-v6-c-expandable-section pf-m-detached">
      <div class="pf-v6-c-expandable-section__toggle">
        <button
          class="pf-v6-c-button pf-m-link"
          id="code-block-expandable-toggle"
          type="button"
          aria-expanded="false"
          aria-controls="code-block-expandable-content"
        >
          <span class="pf-v6-c-button__icon pf-m-start">
            <span
              class="pf-v6-c-expandable-section__toggle-icon pf-m-expand-top"
            >
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
                />
              </svg>
            </span>
          </span>
          <span class="pf-v6-c-button__text">Show more</span>
        </button>
      </div>
    </div>
  </div>
</div>

```

### Expandable expanded

```html
<div class="pf-v6-c-code-block">
  <div class="pf-v6-c-code-block__header">
    <div class="pf-v6-c-code-block__actions">
      <div class="pf-v6-c-code-block__actions-item">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Copy to clipboard expandable expanded example code content"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 448 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M320 448v40c0 13.255-10.745 24-24 24H24c-13.255 0-24-10.745-24-24V120c0-13.255 10.745-24 24-24h72v296c0 30.879 25.121 56 56 56h168zm0-344V0H152c-13.255 0-24 10.745-24 24v368c0 13.255 10.745 24 24 24h272c13.255 0 24-10.745 24-24V128H344c-13.2 0-24-10.8-24-24zm120.971-31.029L375.029 7.029A24 24 0 0 0 358.059 0H352v96h96v-6.059a24 24 0 0 0-7.029-16.97z"
              />
            </svg>
          </span>
        </button>
      </div>
      <div class="pf-v6-c-code-block__actions-item">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Run expandable expanded example code in Web Terminal"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 448 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M424.4 214.7L72.4 6.6C43.8-10.3 0 6.1 0 47.9V464c0 37.5 40.7 60.1 72.4 41.3l352-208c31.4-18.5 31.5-64.1 0-82.6z"
              />
            </svg>
          </span>
        </button>
      </div>
    </div>
  </div>
  <div class="pf-v6-c-code-block__content">
    <pre class="pf-v6-c-code-block__pre"><code class="pf-v6-c-code-block__code">apiVersion: helm.openshift.io/v1beta1/
kind: HelmChartRepository
metadata:
name: azure-sample-repo<div
  class="pf-v6-c-expandable-section pf-m-expanded pf-m-detached"
><div
  class="pf-v6-c-expandable-section__content"
  id="code-block-expandable-expanded-content"
  role="region"
  aria-labelledby="code-block-expandable-expanded-toggle"
>
  spec:
  connectionConfig:
  url: https://raw.githubusercontent.com/Azure-Samples/helm-charts/master/docs</div>
</div>
</code>
</pre>
    <div class="pf-v6-c-expandable-section pf-m-expanded pf-m-detached">
      <div class="pf-v6-c-expandable-section__toggle">
        <button
          class="pf-v6-c-button pf-m-link"
          id="code-block-expandable-expanded-toggle"
          type="button"
          aria-expanded="true"
          aria-controls="code-block-expandable-expanded-content"
        >
          <span class="pf-v6-c-button__icon pf-m-start">
            <span
              class="pf-v6-c-expandable-section__toggle-icon pf-m-expand-top"
            >
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
                />
              </svg>
            </span>
          </span>
          <span class="pf-v6-c-button__text">Show less</span>
        </button>
      </div>
    </div>
  </div>
</div>

```

## Documentation

### Usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-code-block` | `<div>` | Initiates the code block component. **Required** |
| `.pf-v6-c-code-block__header` | `<div>` | Initiates the code block header. |
| `.pf-v6-c-code-block__actions` | `<div>` | Initiates the code block actions. |
| `.pf-v6-c-code-block__actions-item` | `<div>` | Initiates a code block action item. |
| `.pf-v6-c-code-block__content` | `<div>` | Initiates the code block content. **Required** |
| `.pf-v6-c-code-block__pre` | `<pre>` | Initiates the code block `<pre>` element. **Required** |
| `.pf-v6-c-code-block__code` | `<code>` | Initiates the code block `<code>` element. **Required** |
