---
id: Navigation
section: components
cssPrefix: pf-v6-c-nav
---import './Navigation.css'

## Examples

### Default

```html
<nav class="pf-v6-c-nav" aria-label="Global">
  <ul class="pf-v6-c-nav__list" role="list">
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Link 1</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link pf-m-current" aria-current="page">
        <span class="pf-v6-c-nav__link-text">Current link</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Link 3</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Link 4</span>
      </a>
    </li>
  </ul>
</nav>

```

### Grouped nav

```html
<nav class="pf-v6-c-nav" aria-label="Global">
  <section class="pf-v6-c-nav__section" aria-labelledby="grouped-title1">
    <h2 class="pf-v6-c-nav__section-title" id="grouped-title1">Section title 1</h2>
    <ul class="pf-v6-c-nav__list" role="list">
      <li class="pf-v6-c-nav__item">
        <a href="#" class="pf-v6-c-nav__link">
          <span class="pf-v6-c-nav__link-text">Link 1</span>
        </a>
      </li>
      <li class="pf-v6-c-nav__item">
        <a href="#" class="pf-v6-c-nav__link">
          <span class="pf-v6-c-nav__link-text">Link 2</span>
        </a>
      </li>
      <li class="pf-v6-c-nav__item">
        <a href="#" class="pf-v6-c-nav__link">
          <span class="pf-v6-c-nav__link-text">Link 3</span>
        </a>
      </li>
    </ul>
  </section>

  <section class="pf-v6-c-nav__section" aria-labelledby="grouped-title2">
    <h2 class="pf-v6-c-nav__section-title" id="grouped-title2">Section title 2</h2>
    <ul class="pf-v6-c-nav__list" role="list">
      <li class="pf-v6-c-nav__item">
        <a href="#" class="pf-v6-c-nav__link">
          <span class="pf-v6-c-nav__link-text">Link 1</span>
        </a>
      </li>
      <li class="pf-v6-c-nav__item">
        <a href="#" class="pf-v6-c-nav__link pf-m-current" aria-current="page">
          <span class="pf-v6-c-nav__link-text">Current link</span>
        </a>
      </li>
      <li class="pf-v6-c-nav__item">
        <a href="#" class="pf-v6-c-nav__link">
          <span class="pf-v6-c-nav__link-text">Link 3</span>
        </a>
      </li>
    </ul>
  </section>
</nav>

```

### Grouped nav, no titles

```html
<nav class="pf-v6-c-nav" aria-label="Global">
  <section class="pf-v6-c-nav__section" aria-label="Section one">
    <ul class="pf-v6-c-nav__list" role="list">
      <li class="pf-v6-c-nav__item">
        <a href="#" class="pf-v6-c-nav__link">
          <span class="pf-v6-c-nav__link-text">Link 1</span>
        </a>
      </li>
      <li class="pf-v6-c-nav__item">
        <a href="#" class="pf-v6-c-nav__link">
          <span class="pf-v6-c-nav__link-text">Link 2</span>
        </a>
      </li>
      <li class="pf-v6-c-nav__item">
        <a href="#" class="pf-v6-c-nav__link">
          <span class="pf-v6-c-nav__link-text">Link 3</span>
        </a>
      </li>
    </ul>
  </section>
  <hr class="pf-v6-c-divider" />

  <section class="pf-v6-c-nav__section" aria-label="Section two">
    <ul class="pf-v6-c-nav__list" role="list">
      <li class="pf-v6-c-nav__item">
        <a href="#" class="pf-v6-c-nav__link">
          <span class="pf-v6-c-nav__link-text">Section 2, link 1</span>
        </a>
      </li>
      <li class="pf-v6-c-nav__item">
        <a href="#" class="pf-v6-c-nav__link pf-m-current" aria-current="page">
          <span class="pf-v6-c-nav__link-text">Current link</span>
        </a>
      </li>
      <li class="pf-v6-c-nav__item">
        <a href="#" class="pf-v6-c-nav__link">
          <span class="pf-v6-c-nav__link-text">Link 3</span>
        </a>
      </li>
    </ul>
  </section>
</nav>

```

### Expanded

```html
<nav class="pf-v6-c-nav" aria-label="Global">
  <ul class="pf-v6-c-nav__list" role="list">
    <li class="pf-v6-c-nav__item pf-m-expanded">
      <button
        class="pf-v6-c-nav__link"
        aria-expanded="true"
        id="expandable-example1"
      >
        <span
          class="pf-v6-c-nav__link-text"
        >Link 1 (current and expanded example)</span>
        <span class="pf-v6-c-nav__toggle">
          <span class="pf-v6-c-nav__toggle-icon">
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
      </button>
      <section
        class="pf-v6-c-nav__subnav"
        aria-labelledby="expandable-example1"
      >
        <ul class="pf-v6-c-nav__list" role="list">
          <li class="pf-v6-c-nav__item">
            <a href="#" class="pf-v6-c-nav__link">
              <span class="pf-v6-c-nav__link-text">Current link</span>
            </a>
          </li>
          <li class="pf-v6-c-nav__item">
            <a href="#" class="pf-v6-c-nav__link">
              <span class="pf-v6-c-nav__link-text">Subnav link 2</span>
            </a>
          </li>
          <li class="pf-v6-c-nav__item">
            <a
              href="#"
              class="pf-v6-c-nav__link pf-m-current"
              aria-current="page"
            >
              <span class="pf-v6-c-nav__link-text">Subnav link 3</span>
            </a>
          </li>
        </ul>
      </section>
    </li>
    <li class="pf-v6-c-nav__item pf-m-expanded">
      <button
        class="pf-v6-c-nav__link"
        aria-expanded="true"
        id="expandable-example2"
      >
        <span
          class="pf-v6-c-nav__link-text"
        >Link 2 (expanded, but not current example)</span>
        <span class="pf-v6-c-nav__toggle">
          <span class="pf-v6-c-nav__toggle-icon">
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
      </button>
      <section
        class="pf-v6-c-nav__subnav"
        aria-labelledby="expandable-example2"
      >
        <ul class="pf-v6-c-nav__list" role="list">
          <li class="pf-v6-c-nav__item">
            <a href="#" class="pf-v6-c-nav__link">
              <span class="pf-v6-c-nav__link-text">Subnav link 1</span>
            </a>
          </li>
          <li class="pf-v6-c-nav__item">
            <a href="#" class="pf-v6-c-nav__link">
              <span class="pf-v6-c-nav__link-text">Subnav link 2</span>
            </a>
          </li>
        </ul>
      </section>
    </li>
    <li class="pf-v6-c-nav__item">
      <button
        class="pf-v6-c-nav__link"
        aria-expanded="false"
        id="expandable-example3"
      >
        <span class="pf-v6-c-nav__link-text">Link 3</span>
        <span class="pf-v6-c-nav__toggle">
          <span class="pf-v6-c-nav__toggle-icon">
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
      </button>
      <section
        class="pf-v6-c-nav__subnav"
        aria-labelledby="expandable-example3"
        hidden
        inert
      >
        <ul class="pf-v6-c-nav__list" role="list">
          <li class="pf-v6-c-nav__item">
            <a href="#" class="pf-v6-c-nav__link">
              <span class="pf-v6-c-nav__link-text">Subnav link 1</span>
            </a>
          </li>
          <li class="pf-v6-c-nav__item">
            <a href="#" class="pf-v6-c-nav__link">
              <span class="pf-v6-c-nav__link-text">Subnav link 2</span>
            </a>
          </li>
        </ul>
      </section>
    </li>
  </ul>
</nav>

```

### Expanded with subnav titles

```html
<nav class="pf-v6-c-nav" aria-label="Global">
  <ul class="pf-v6-c-nav__list" role="list">
    <li class="pf-v6-c-nav__item pf-m-expanded">
      <button class="pf-v6-c-nav__link" aria-expanded="true">
        <span class="pf-v6-c-nav__link-text">Link 1</span>
        <span class="pf-v6-c-nav__toggle">
          <span class="pf-v6-c-nav__toggle-icon">
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
      </button>
      <section class="pf-v6-c-nav__subnav" aria-labelledby="subnav-title1">
        <ul class="pf-v6-c-nav__list" role="list">
          <li class="pf-v6-c-nav__item">
            <a href="#" class="pf-v6-c-nav__link">
              <span class="pf-v6-c-nav__link-text">Current link</span>
            </a>
          </li>
          <li class="pf-v6-c-nav__item">
            <a
              href="#"
              class="pf-v6-c-nav__link pf-m-current"
              aria-current="page"
            >
              <span class="pf-v6-c-nav__link-text">Subnav link 2</span>
            </a>
          </li>
          <li class="pf-v6-c-nav__item">
            <a href="#" class="pf-v6-c-nav__link">
              <span class="pf-v6-c-nav__link-text">Subnav link 3</span>
            </a>
          </li>
        </ul>
      </section>
    </li>
    <li class="pf-v6-c-nav__item pf-m-expanded">
      <button class="pf-v6-c-nav__link" aria-expanded="true">
        <span class="pf-v6-c-nav__link-text">Link 2</span>
        <span class="pf-v6-c-nav__toggle">
          <span class="pf-v6-c-nav__toggle-icon">
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
      </button>
      <section class="pf-v6-c-nav__subnav" aria-labelledby="subnav-title2">
        <ul class="pf-v6-c-nav__list" role="list">
          <li class="pf-v6-c-nav__item">
            <a href="#" class="pf-v6-c-nav__link">
              <span class="pf-v6-c-nav__link-text">Subnav link 1</span>
            </a>
          </li>
          <li class="pf-v6-c-nav__item">
            <a href="#" class="pf-v6-c-nav__link">
              <span class="pf-v6-c-nav__link-text">Subnav link 2</span>
            </a>
          </li>
        </ul>
      </section>
    </li>
  </ul>
</nav>

```

### Mixed

```html
<nav class="pf-v6-c-nav" aria-label="Global">
  <ul class="pf-v6-c-nav__list" role="list">
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Link 1 (not expandable)</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item pf-m-expanded">
      <button
        class="pf-v6-c-nav__link"
        aria-expanded="true"
        id="nav-mixed-link2"
      >
        <span
          class="pf-v6-c-nav__link-text"
        >Link 2 (expanded, but not current example)</span>
        <span class="pf-v6-c-nav__toggle">
          <span class="pf-v6-c-nav__toggle-icon">
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
      </button>
      <section class="pf-v6-c-nav__subnav" aria-labelledby="nav-mixed-link2">
        <ul class="pf-v6-c-nav__list" role="list">
          <li class="pf-v6-c-nav__item">
            <a href="#" class="pf-v6-c-nav__link">
              <span class="pf-v6-c-nav__link-text">Subnav link 1</span>
            </a>
          </li>
          <li class="pf-v6-c-nav__item">
            <a href="#" class="pf-v6-c-nav__link">
              <span class="pf-v6-c-nav__link-text">Subnav link 2</span>
            </a>
          </li>
        </ul>
      </section>
    </li>
    <li class="pf-v6-c-nav__item">
      <button
        class="pf-v6-c-nav__link"
        aria-expanded="false"
        id="nav-mixed-link4"
      >
        <span
          class="pf-v6-c-nav__link-text"
        >Link 3 (current, but not expanded example)</span>
        <span class="pf-v6-c-nav__toggle">
          <span class="pf-v6-c-nav__toggle-icon">
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
      </button>
      <section
        class="pf-v6-c-nav__subnav"
        aria-labelledby="nav-mixed-link4"
        hidden
        inert
      >
        <ul class="pf-v6-c-nav__list" role="list">
          <li class="pf-v6-c-nav__item">
            <a href="#" class="pf-v6-c-nav__link">
              <span class="pf-v6-c-nav__link-text">Subnav link 1</span>
            </a>
          </li>
          <li class="pf-v6-c-nav__item">
            <a
              href="#"
              class="pf-v6-c-nav__link pf-m-current"
              aria-current="page"
            >
              <span class="pf-v6-c-nav__link-text">Subnav link 2</span>
            </a>
          </li>
          <li class="pf-v6-c-nav__item">
            <a href="#" class="pf-v6-c-nav__link">
              <span class="pf-v6-c-nav__link-text">Subnav link 3</span>
            </a>
          </li>
        </ul>
      </section>
    </li>
  </ul>
</nav>

```

### Expandable, third level

```html
<nav class="pf-v6-c-nav" aria-label="Global">
  <ul class="pf-v6-c-nav__list" role="list">
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Clusters</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Overview</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Releases</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <button
        class="pf-v6-c-nav__link"
        aria-expanded="false"
        id="expandable-third-level-example-example-1"
      >
        <span class="pf-v6-c-nav__link-text">Subscriptions</span>
        <span class="pf-v6-c-nav__toggle">
          <span class="pf-v6-c-nav__toggle-icon">
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
      </button>
      <section
        class="pf-v6-c-nav__subnav"
        aria-labelledby="expandable-third-level-example-example-1"
        hidden
        inert
      >
        <ul class="pf-v6-c-nav__list" role="list">
          <li class="pf-v6-c-nav__item">
            <a href="#" class="pf-v6-c-nav__link">
              <span class="pf-v6-c-nav__link-text">Subnav link 1</span>
            </a>
          </li>
          <li class="pf-v6-c-nav__item">
            <a href="#" class="pf-v6-c-nav__link">
              <span class="pf-v6-c-nav__link-text">Subnav link 2</span>
            </a>
          </li>
        </ul>
      </section>
    </li>
    <li class="pf-v6-c-nav__item pf-m-expanded">
      <button
        class="pf-v6-c-nav__link"
        aria-expanded="true"
        id="expandable-third-level-example-example-2"
      >
        <span class="pf-v6-c-nav__link-text">Cost management</span>
        <span class="pf-v6-c-nav__toggle">
          <span class="pf-v6-c-nav__toggle-icon">
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
      </button>
      <section
        class="pf-v6-c-nav__subnav"
        aria-labelledby="expandable-third-level-example-example-2"
      >
        <ul class="pf-v6-c-nav__list" role="list">
          <li class="pf-v6-c-nav__item">
            <a href="#" class="pf-v6-c-nav__link">
              <span class="pf-v6-c-nav__link-text">Overview</span>
            </a>
          </li>
          <li class="pf-v6-c-nav__item">
            <a href="#" class="pf-v6-c-nav__link">
              <span class="pf-v6-c-nav__link-text">Openshift</span>
            </a>
          </li>
          <li class="pf-v6-c-nav__item pf-m-expanded">
            <button
              class="pf-v6-c-nav__link"
              aria-expanded="true"
              id="-sub-example-1"
            >
              <span class="pf-v6-c-nav__link-text">Public clouds</span>
              <span class="pf-v6-c-nav__toggle">
                <span class="pf-v6-c-nav__toggle-icon">
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
            </button>
            <section
              class="pf-v6-c-nav__subnav"
              aria-labelledby="-sub-example-1"
            >
              <ul class="pf-v6-c-nav__list" role="list">
                <li class="pf-v6-c-nav__item">
                  <a href="#" class="pf-v6-c-nav__link">
                    <span class="pf-v6-c-nav__link-text">Amazon Web Services</span>
                  </a>
                </li>
                <li class="pf-v6-c-nav__item">
                  <a href="#" class="pf-v6-c-nav__link">
                    <span class="pf-v6-c-nav__link-text">Microsoft Azure</span>
                  </a>
                </li>
                <li class="pf-v6-c-nav__item">
                  <a href="#" class="pf-v6-c-nav__link">
                    <span class="pf-v6-c-nav__link-text">Google Cloud Services</span>
                  </a>
                </li>
              </ul>
            </section>
          </li>
          <li class="pf-v6-c-nav__item">
            <a href="#" class="pf-v6-c-nav__link">
              <span class="pf-v6-c-nav__link-text">Cost Models</span>
            </a>
          </li>
          <li class="pf-v6-c-nav__item">
            <a href="#" class="pf-v6-c-nav__link">
              <span class="pf-v6-c-nav__link-text">Cost Explorer</span>
            </a>
          </li>
        </ul>
      </section>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Support Cases</span>
      </a>
    </li>
  </ul>
</nav>

```

### Horizontal

```html
<nav class="pf-v6-c-nav pf-m-horizontal" aria-label="Global">
  <ul class="pf-v6-c-nav__list" role="list">
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link pf-m-current" aria-current="page">
        <span class="pf-v6-c-nav__link-text">Item 1</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Item 2</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Item 3</span>
      </a>
    </li>
  </ul>
</nav>

```

### Horizontal overflow

```html
<nav class="pf-v6-c-nav pf-m-scrollable pf-m-horizontal" aria-label="Global">
  <div class="pf-v6-c-nav__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll start"
      disabled
    >
      <span class="pf-v6-c-button__icon">
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
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul class="pf-v6-c-nav__list" role="list">
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Horizontal nav item 1</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Horizontal nav item 2</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Horizontal nav item 3</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Horizontal nav item 4</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link pf-m-current" aria-current="page">
        <span class="pf-v6-c-nav__link-text">Horizontal nav item 5</span>
      </a>
    </li>
  </ul>
  <div class="pf-v6-c-nav__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll end"
    >
      <span class="pf-v6-c-button__icon">
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
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</nav>

```

### Horizontal subnav

```html
<nav class="pf-v6-c-nav pf-m-horizontal pf-m-subnav" aria-label="Local">
  <ul class="pf-v6-c-nav__list" role="list">
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link pf-m-current" aria-current="page">
        <span class="pf-v6-c-nav__link-text">Item 1</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Item 2</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Item 3</span>
      </a>
    </li>
  </ul>
</nav>

```

### Horizontal subnav overflow

```html
<nav
  class="pf-v6-c-nav pf-m-scrollable pf-m-horizontal pf-m-subnav"
  aria-label="Global"
>
  <div class="pf-v6-c-nav__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll start"
      disabled
    >
      <span class="pf-v6-c-button__icon">
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
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul class="pf-v6-c-nav__list" role="list">
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Horizontal nav item 1</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Horizontal nav item 2</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Horizontal nav item 3</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Horizontal nav item 4</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link pf-m-current" aria-current="page">
        <span class="pf-v6-c-nav__link-text">Horizontal nav item 5</span>
      </a>
    </li>
  </ul>
  <div class="pf-v6-c-nav__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll end"
    >
      <span class="pf-v6-c-button__icon">
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
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</nav>

```

### Nav with flyout

```html
<nav class="pf-v6-c-nav" aria-label="Global">
  <ul class="pf-v6-c-nav__list" role="list">
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Clusters</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Overview</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Releases</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item pf-m-flyout">
      <a
        href="#"
        class="pf-v6-c-nav__link pf-m-current"
        aria-current="page"
        aria-haspopup="true"
        aria-expanded="true"
      >
        <span class="pf-v6-c-nav__link-text">Subscriptions</span>
        <span class="pf-v6-c-nav__toggle">
          <span class="pf-v6-c-nav__toggle-icon">
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
                d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
              />
            </svg>
          </span>
        </span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Support cases</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Cluster manager feedback</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Red Hat Marketplace</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-text">Documentation</span>
      </a>
    </li>
  </ul>
  <div class="pf-v6-c-menu pf-m-flyout pf-m-nav">
    <div class="pf-v6-c-menu__content">
      <ul class="pf-v6-c-menu__list" role="menu">
        <li class="pf-v6-c-menu__list-item" role="none">
          <a class="pf-v6-c-menu__item" href="#" role="menuitem">
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">Container platform</span>
            </span>
          </a>
        </li>
        <li class="pf-v6-c-menu__list-item" role="none">
          <button
            class="pf-v6-c-menu__item"
            type="button"
            role="menuitem"
            aria-expanded="true"
          >
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">Dedicated</span>
              <span class="pf-v6-c-menu__item-toggle-icon">
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
                    d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                  />
                </svg>
              </span>
            </span>
          </button>
          <div class="pf-v6-c-menu">
            <div class="pf-v6-c-menu__content">
              <ul class="pf-v6-c-menu__list" role="menu">
                <li class="pf-v6-c-menu__list-item" role="none">
                  <a class="pf-v6-c-menu__item" href="#" role="menuitem">
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-text">Dedicated (Annual)</span>
                    </span>
                  </a>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <a class="pf-v6-c-menu__item" href="#" role="menuitem">
                    <span class="pf-v6-c-menu__item-main">
                      <span
                        class="pf-v6-c-menu__item-text"
                      >Dedicated (On-Demand)</span>
                    </span>
                  </a>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <a class="pf-v6-c-menu__item" href="#" role="menuitem">
                    <span class="pf-v6-c-menu__item-main">
                      <span
                        class="pf-v6-c-menu__item-text"
                      >Dedicated (On-Demand limits)</span>
                    </span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</nav>

```

### Nav with drilldown menu

```html
<nav class="pf-v6-c-nav" aria-label="Drilldown menu example">
  <div class="pf-v6-c-menu pf-m-drilldown">
    <div class="pf-v6-c-menu__content">
      <ul class="pf-v6-c-menu__list" role="menu">
        <li class="pf-v6-c-menu__list-item" role="none">
          <button class="pf-v6-c-menu__item" type="button" role="menuitem">
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">Start rollout</span>
            </span>
          </button>
        </li>
        <li class="pf-v6-c-menu__list-item" role="none">
          <button class="pf-v6-c-menu__item" type="button" role="menuitem">
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">Pause rollout</span>
            </span>
          </button>
        </li>
        <li class="pf-v6-c-menu__list-item" role="none">
          <button
            class="pf-v6-c-menu__item pf-m-current"
            type="button"
            role="menuitem"
          >
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">Current link</span>
            </span>
          </button>
        </li>
        <li class="pf-v6-c-menu__list-item" role="none">
          <button class="pf-v6-c-menu__item" type="button" role="menuitem">
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">Add storage</span>
            </span>
          </button>
        </li>
        <li class="pf-v6-c-menu__list-item" role="none">
          <button
            class="pf-v6-c-menu__item"
            type="button"
            role="menuitem"
            aria-expanded="false"
          >
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">Edit</span>
              <span class="pf-v6-c-menu__item-toggle-icon">
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
                    d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                  />
                </svg>
              </span>
            </span>
          </button>
          <div class="pf-v6-c-menu">
            <div class="pf-v6-c-menu__content">
              <ul class="pf-v6-c-menu__list" role="menu">
                <li class="pf-v6-c-menu__list-item pf-m-drill-up" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                    tabindex="0"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-toggle-icon">
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
                            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                          />
                        </svg>
                      </span>
                      <span class="pf-v6-c-menu__item-text">Edit</span>
                    </span>
                  </button>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                    aria-expanded="false"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-text">Deployment</span>
                      <span class="pf-v6-c-menu__item-toggle-icon">
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
                            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                          />
                        </svg>
                      </span>
                    </span>
                  </button>
                  <div class="pf-v6-c-menu">
                    <div class="pf-v6-c-menu__content">
                      <ul class="pf-v6-c-menu__list" role="menu">
                        <li
                          class="pf-v6-c-menu__list-item pf-m-drill-up"
                          role="none"
                        >
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                            tabindex="0"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-toggle-icon">
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
                                    d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                                  />
                                </svg>
                              </span>
                              <span class="pf-v6-c-menu__item-text">Deployment</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Routes</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Nodes</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">URLs</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                            aria-expanded="false"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span
                                class="pf-v6-c-menu__item-text"
                              >Advanced settings</span>
                              <span class="pf-v6-c-menu__item-toggle-icon">
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
                                    d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                                  />
                                </svg>
                              </span>
                            </span>
                          </button>
                          <div class="pf-v6-c-menu">
                            <div class="pf-v6-c-menu__content">
                              <ul class="pf-v6-c-menu__list" role="menu">
                                <li
                                  class="pf-v6-c-menu__list-item pf-m-drill-up"
                                  role="none"
                                >
                                  <button
                                    class="pf-v6-c-menu__item"
                                    type="button"
                                    role="menuitem"
                                    tabindex="0"
                                  >
                                    <span class="pf-v6-c-menu__item-main">
                                      <span
                                        class="pf-v6-c-menu__item-toggle-icon"
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
                                            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                                          />
                                        </svg>
                                      </span>
                                      <span
                                        class="pf-v6-c-menu__item-text"
                                      >Advanced settings</span>
                                    </span>
                                  </button>
                                </li>
                                <li class="pf-v6-c-menu__list-item" role="none">
                                  <button
                                    class="pf-v6-c-menu__item"
                                    type="button"
                                    role="menuitem"
                                  >
                                    <span class="pf-v6-c-menu__item-main">
                                      <span
                                        class="pf-v6-c-menu__item-text"
                                      >Reports</span>
                                    </span>
                                  </button>
                                </li>
                                <li class="pf-v6-c-menu__list-item" role="none">
                                  <button
                                    class="pf-v6-c-menu__item"
                                    type="button"
                                    role="menuitem"
                                  >
                                    <span class="pf-v6-c-menu__item-main">
                                      <span
                                        class="pf-v6-c-menu__item-text"
                                      >Policies</span>
                                    </span>
                                  </button>
                                </li>
                                <li class="pf-v6-c-menu__list-item" role="none">
                                  <button
                                    class="pf-v6-c-menu__item"
                                    type="button"
                                    role="menuitem"
                                  >
                                    <span class="pf-v6-c-menu__item-main">
                                      <span
                                        class="pf-v6-c-menu__item-text"
                                      >Systems</span>
                                    </span>
                                  </button>
                                </li>
                              </ul>
                            </div>
                          </div>
                        </li>
                      </ul>
                    </div>
                  </div>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                    aria-expanded="false"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-text">RBAC</span>
                      <span class="pf-v6-c-menu__item-toggle-icon">
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
                            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                          />
                        </svg>
                      </span>
                    </span>
                  </button>
                  <div class="pf-v6-c-menu">
                    <div class="pf-v6-c-menu__content">
                      <ul class="pf-v6-c-menu__list" role="menu">
                        <li
                          class="pf-v6-c-menu__list-item pf-m-drill-up"
                          role="none"
                        >
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-toggle-icon">
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
                                    d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                                  />
                                </svg>
                              </span>
                              <span class="pf-v6-c-menu__item-text">RBAC</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Reports</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Policies</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Systems</span>
                            </span>
                          </button>
                        </li>
                      </ul>
                    </div>
                  </div>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span
                        class="pf-v6-c-menu__item-text"
                      >Thing with a longer label</span>
                    </span>
                  </button>
                </li>
              </ul>
            </div>
          </div>
        </li>
        <li class="pf-v6-c-menu__list-item" role="none">
          <button
            class="pf-v6-c-menu__item"
            type="button"
            role="menuitem"
            aria-expanded="false"
          >
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">Configuration</span>
              <span class="pf-v6-c-menu__item-toggle-icon">
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
                    d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                  />
                </svg>
              </span>
            </span>
          </button>
          <div class="pf-v6-c-menu">
            <div class="pf-v6-c-menu__content">
              <ul class="pf-v6-c-menu__list" role="menu">
                <li class="pf-v6-c-menu__list-item pf-m-drill-up" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-toggle-icon">
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
                            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                          />
                        </svg>
                      </span>
                      <span class="pf-v6-c-menu__item-text">Configuration</span>
                    </span>
                  </button>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                    aria-expanded="false"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-text">Profile</span>
                      <span class="pf-v6-c-menu__item-toggle-icon">
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
                            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                          />
                        </svg>
                      </span>
                    </span>
                  </button>
                  <div class="pf-v6-c-menu">
                    <div class="pf-v6-c-menu__content">
                      <ul class="pf-v6-c-menu__list" role="menu">
                        <li
                          class="pf-v6-c-menu__list-item pf-m-drill-up"
                          role="none"
                        >
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-toggle-icon">
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
                                    d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                                  />
                                </svg>
                              </span>
                              <span class="pf-v6-c-menu__item-text">Profile</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Avatar</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Name</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Title</span>
                            </span>
                          </button>
                        </li>
                      </ul>
                    </div>
                  </div>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-text">Time zone</span>
                    </span>
                  </button>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-text">Account settings</span>
                    </span>
                  </button>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span
                        class="pf-v6-c-menu__item-text"
                      >Thing with a longer label</span>
                    </span>
                  </button>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                    aria-expanded="false"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-text">Edit access settings</span>
                      <span class="pf-v6-c-menu__item-toggle-icon">
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
                            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                          />
                        </svg>
                      </span>
                    </span>
                  </button>
                  <div class="pf-v6-c-menu">
                    <div class="pf-v6-c-menu__content">
                      <ul class="pf-v6-c-menu__list" role="menu">
                        <li
                          class="pf-v6-c-menu__list-item pf-m-drill-up"
                          role="none"
                        >
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-toggle-icon">
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
                                    d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                                  />
                                </svg>
                              </span>
                              <span
                                class="pf-v6-c-menu__item-text"
                              >Edit access settings</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span
                                class="pf-v6-c-menu__item-text"
                              >Global access</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span
                                class="pf-v6-c-menu__item-text"
                              >Account access</span>
                            </span>
                          </button>
                        </li>
                      </ul>
                    </div>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</nav>

```

### Nav with drilldown menu level two

```html
<nav class="pf-v6-c-nav" aria-label="Drilldown menu example">
  <div class="pf-v6-c-menu pf-m-drilldown pf-m-drilled-in">
    <div
      class="pf-v6-c-menu__content"
      style="--pf-v6-c-menu__content--Height: 228px;"
    >
      <ul class="pf-v6-c-menu__list" role="menu">
        <li class="pf-v6-c-menu__list-item" role="none">
          <button class="pf-v6-c-menu__item" type="button" role="menuitem">
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">Start rollout</span>
            </span>
          </button>
        </li>
        <li class="pf-v6-c-menu__list-item" role="none">
          <button class="pf-v6-c-menu__item" type="button" role="menuitem">
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">Pause rollout</span>
            </span>
          </button>
        </li>
        <li class="pf-v6-c-menu__list-item" role="none">
          <button
            class="pf-v6-c-menu__item pf-m-current"
            type="button"
            role="menuitem"
          >
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">Current link</span>
            </span>
          </button>
        </li>
        <li class="pf-v6-c-menu__list-item" role="none">
          <button class="pf-v6-c-menu__item" type="button" role="menuitem">
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">Add storage</span>
            </span>
          </button>
        </li>
        <li class="pf-v6-c-menu__list-item pf-m-current-path" role="none">
          <button
            class="pf-v6-c-menu__item"
            type="button"
            role="menuitem"
            aria-expanded="true"
          >
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">Edit</span>
              <span class="pf-v6-c-menu__item-toggle-icon">
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
                    d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                  />
                </svg>
              </span>
            </span>
          </button>
          <div class="pf-v6-c-menu">
            <div class="pf-v6-c-menu__content">
              <ul class="pf-v6-c-menu__list" role="menu">
                <li class="pf-v6-c-menu__list-item pf-m-drill-up" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                    tabindex="0"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-toggle-icon">
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
                            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                          />
                        </svg>
                      </span>
                      <span class="pf-v6-c-menu__item-text">Edit</span>
                    </span>
                  </button>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                    aria-expanded="false"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-text">Deployment</span>
                      <span class="pf-v6-c-menu__item-toggle-icon">
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
                            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                          />
                        </svg>
                      </span>
                    </span>
                  </button>
                  <div class="pf-v6-c-menu">
                    <div class="pf-v6-c-menu__content">
                      <ul class="pf-v6-c-menu__list" role="menu">
                        <li
                          class="pf-v6-c-menu__list-item pf-m-drill-up"
                          role="none"
                        >
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                            tabindex="0"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-toggle-icon">
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
                                    d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                                  />
                                </svg>
                              </span>
                              <span class="pf-v6-c-menu__item-text">Deployment</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Routes</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Nodes</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">URLs</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                            aria-expanded="false"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span
                                class="pf-v6-c-menu__item-text"
                              >Advanced settings</span>
                              <span class="pf-v6-c-menu__item-toggle-icon">
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
                                    d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                                  />
                                </svg>
                              </span>
                            </span>
                          </button>
                          <div class="pf-v6-c-menu">
                            <div class="pf-v6-c-menu__content">
                              <ul class="pf-v6-c-menu__list" role="menu">
                                <li
                                  class="pf-v6-c-menu__list-item pf-m-drill-up"
                                  role="none"
                                >
                                  <button
                                    class="pf-v6-c-menu__item"
                                    type="button"
                                    role="menuitem"
                                    tabindex="0"
                                  >
                                    <span class="pf-v6-c-menu__item-main">
                                      <span
                                        class="pf-v6-c-menu__item-toggle-icon"
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
                                            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                                          />
                                        </svg>
                                      </span>
                                      <span
                                        class="pf-v6-c-menu__item-text"
                                      >Advanced settings</span>
                                    </span>
                                  </button>
                                </li>
                                <li class="pf-v6-c-menu__list-item" role="none">
                                  <button
                                    class="pf-v6-c-menu__item"
                                    type="button"
                                    role="menuitem"
                                  >
                                    <span class="pf-v6-c-menu__item-main">
                                      <span
                                        class="pf-v6-c-menu__item-text"
                                      >Reports</span>
                                    </span>
                                  </button>
                                </li>
                                <li class="pf-v6-c-menu__list-item" role="none">
                                  <button
                                    class="pf-v6-c-menu__item"
                                    type="button"
                                    role="menuitem"
                                  >
                                    <span class="pf-v6-c-menu__item-main">
                                      <span
                                        class="pf-v6-c-menu__item-text"
                                      >Policies</span>
                                    </span>
                                  </button>
                                </li>
                                <li class="pf-v6-c-menu__list-item" role="none">
                                  <button
                                    class="pf-v6-c-menu__item"
                                    type="button"
                                    role="menuitem"
                                  >
                                    <span class="pf-v6-c-menu__item-main">
                                      <span
                                        class="pf-v6-c-menu__item-text"
                                      >Systems</span>
                                    </span>
                                  </button>
                                </li>
                              </ul>
                            </div>
                          </div>
                        </li>
                      </ul>
                    </div>
                  </div>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                    aria-expanded="false"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-text">RBAC</span>
                      <span class="pf-v6-c-menu__item-toggle-icon">
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
                            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                          />
                        </svg>
                      </span>
                    </span>
                  </button>
                  <div class="pf-v6-c-menu">
                    <div class="pf-v6-c-menu__content">
                      <ul class="pf-v6-c-menu__list" role="menu">
                        <li
                          class="pf-v6-c-menu__list-item pf-m-drill-up"
                          role="none"
                        >
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-toggle-icon">
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
                                    d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                                  />
                                </svg>
                              </span>
                              <span class="pf-v6-c-menu__item-text">RBAC</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Reports</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Policies</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Systems</span>
                            </span>
                          </button>
                        </li>
                      </ul>
                    </div>
                  </div>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span
                        class="pf-v6-c-menu__item-text"
                      >Thing with a longer label</span>
                    </span>
                  </button>
                </li>
              </ul>
            </div>
          </div>
        </li>
        <li class="pf-v6-c-menu__list-item" role="none">
          <button
            class="pf-v6-c-menu__item"
            type="button"
            role="menuitem"
            aria-expanded="false"
          >
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">Configuration</span>
              <span class="pf-v6-c-menu__item-toggle-icon">
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
                    d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                  />
                </svg>
              </span>
            </span>
          </button>
          <div class="pf-v6-c-menu">
            <div class="pf-v6-c-menu__content">
              <ul class="pf-v6-c-menu__list" role="menu">
                <li class="pf-v6-c-menu__list-item pf-m-drill-up" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-toggle-icon">
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
                            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                          />
                        </svg>
                      </span>
                      <span class="pf-v6-c-menu__item-text">Configuration</span>
                    </span>
                  </button>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                    aria-expanded="false"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-text">Profile</span>
                      <span class="pf-v6-c-menu__item-toggle-icon">
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
                            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                          />
                        </svg>
                      </span>
                    </span>
                  </button>
                  <div class="pf-v6-c-menu">
                    <div class="pf-v6-c-menu__content">
                      <ul class="pf-v6-c-menu__list" role="menu">
                        <li
                          class="pf-v6-c-menu__list-item pf-m-drill-up"
                          role="none"
                        >
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-toggle-icon">
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
                                    d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                                  />
                                </svg>
                              </span>
                              <span class="pf-v6-c-menu__item-text">Profile</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Avatar</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Name</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Title</span>
                            </span>
                          </button>
                        </li>
                      </ul>
                    </div>
                  </div>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-text">Time zone</span>
                    </span>
                  </button>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-text">Account settings</span>
                    </span>
                  </button>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span
                        class="pf-v6-c-menu__item-text"
                      >Thing with a longer label</span>
                    </span>
                  </button>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                    aria-expanded="false"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-text">Edit access settings</span>
                      <span class="pf-v6-c-menu__item-toggle-icon">
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
                            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                          />
                        </svg>
                      </span>
                    </span>
                  </button>
                  <div class="pf-v6-c-menu">
                    <div class="pf-v6-c-menu__content">
                      <ul class="pf-v6-c-menu__list" role="menu">
                        <li
                          class="pf-v6-c-menu__list-item pf-m-drill-up"
                          role="none"
                        >
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-toggle-icon">
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
                                    d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                                  />
                                </svg>
                              </span>
                              <span
                                class="pf-v6-c-menu__item-text"
                              >Edit access settings</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span
                                class="pf-v6-c-menu__item-text"
                              >Global access</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span
                                class="pf-v6-c-menu__item-text"
                              >Account access</span>
                            </span>
                          </button>
                        </li>
                      </ul>
                    </div>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</nav>

```

### Nav with drilldown menu level three

```html
<nav class="pf-v6-c-nav" aria-label="Drilldown menu example">
  <div class="pf-v6-c-menu pf-m-drilldown pf-m-drilled-in">
    <div
      class="pf-v6-c-menu__content"
      style="--pf-v6-c-menu__content--Height: 284px;"
    >
      <ul class="pf-v6-c-menu__list" role="menu">
        <li class="pf-v6-c-menu__list-item" role="none">
          <button class="pf-v6-c-menu__item" type="button" role="menuitem">
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">Start rollout</span>
            </span>
          </button>
        </li>
        <li class="pf-v6-c-menu__list-item" role="none">
          <button class="pf-v6-c-menu__item" type="button" role="menuitem">
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">Pause rollout</span>
            </span>
          </button>
        </li>
        <li class="pf-v6-c-menu__list-item" role="none">
          <button
            class="pf-v6-c-menu__item pf-m-current"
            type="button"
            role="menuitem"
          >
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">Current link</span>
            </span>
          </button>
        </li>
        <li class="pf-v6-c-menu__list-item" role="none">
          <button class="pf-v6-c-menu__item" type="button" role="menuitem">
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">Add storage</span>
            </span>
          </button>
        </li>
        <li class="pf-v6-c-menu__list-item pf-m-current-path" role="none">
          <button
            class="pf-v6-c-menu__item"
            type="button"
            role="menuitem"
            aria-expanded="true"
          >
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">Edit</span>
              <span class="pf-v6-c-menu__item-toggle-icon">
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
                    d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                  />
                </svg>
              </span>
            </span>
          </button>
          <div class="pf-v6-c-menu pf-m-drilled-in">
            <div class="pf-v6-c-menu__content">
              <ul class="pf-v6-c-menu__list" role="menu">
                <li class="pf-v6-c-menu__list-item pf-m-drill-up" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                    tabindex="0"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-toggle-icon">
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
                            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                          />
                        </svg>
                      </span>
                      <span class="pf-v6-c-menu__item-text">Edit</span>
                    </span>
                  </button>
                </li>
                <li
                  class="pf-v6-c-menu__list-item pf-m-current-path"
                  role="none"
                >
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                    aria-expanded="true"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-text">Deployment</span>
                      <span class="pf-v6-c-menu__item-toggle-icon">
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
                            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                          />
                        </svg>
                      </span>
                    </span>
                  </button>
                  <div class="pf-v6-c-menu">
                    <div class="pf-v6-c-menu__content">
                      <ul class="pf-v6-c-menu__list" role="menu">
                        <li
                          class="pf-v6-c-menu__list-item pf-m-drill-up"
                          role="none"
                        >
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                            tabindex="0"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-toggle-icon">
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
                                    d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                                  />
                                </svg>
                              </span>
                              <span class="pf-v6-c-menu__item-text">Deployment</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Routes</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Nodes</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">URLs</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                            aria-expanded="false"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span
                                class="pf-v6-c-menu__item-text"
                              >Advanced settings</span>
                              <span class="pf-v6-c-menu__item-toggle-icon">
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
                                    d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                                  />
                                </svg>
                              </span>
                            </span>
                          </button>
                          <div class="pf-v6-c-menu">
                            <div class="pf-v6-c-menu__content">
                              <ul class="pf-v6-c-menu__list" role="menu">
                                <li
                                  class="pf-v6-c-menu__list-item pf-m-drill-up"
                                  role="none"
                                >
                                  <button
                                    class="pf-v6-c-menu__item"
                                    type="button"
                                    role="menuitem"
                                    tabindex="0"
                                  >
                                    <span class="pf-v6-c-menu__item-main">
                                      <span
                                        class="pf-v6-c-menu__item-toggle-icon"
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
                                            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                                          />
                                        </svg>
                                      </span>
                                      <span
                                        class="pf-v6-c-menu__item-text"
                                      >Advanced settings</span>
                                    </span>
                                  </button>
                                </li>
                                <li class="pf-v6-c-menu__list-item" role="none">
                                  <button
                                    class="pf-v6-c-menu__item"
                                    type="button"
                                    role="menuitem"
                                  >
                                    <span class="pf-v6-c-menu__item-main">
                                      <span
                                        class="pf-v6-c-menu__item-text"
                                      >Reports</span>
                                    </span>
                                  </button>
                                </li>
                                <li class="pf-v6-c-menu__list-item" role="none">
                                  <button
                                    class="pf-v6-c-menu__item"
                                    type="button"
                                    role="menuitem"
                                  >
                                    <span class="pf-v6-c-menu__item-main">
                                      <span
                                        class="pf-v6-c-menu__item-text"
                                      >Policies</span>
                                    </span>
                                  </button>
                                </li>
                                <li class="pf-v6-c-menu__list-item" role="none">
                                  <button
                                    class="pf-v6-c-menu__item"
                                    type="button"
                                    role="menuitem"
                                  >
                                    <span class="pf-v6-c-menu__item-main">
                                      <span
                                        class="pf-v6-c-menu__item-text"
                                      >Systems</span>
                                    </span>
                                  </button>
                                </li>
                              </ul>
                            </div>
                          </div>
                        </li>
                      </ul>
                    </div>
                  </div>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                    aria-expanded="false"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-text">RBAC</span>
                      <span class="pf-v6-c-menu__item-toggle-icon">
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
                            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                          />
                        </svg>
                      </span>
                    </span>
                  </button>
                  <div class="pf-v6-c-menu">
                    <div class="pf-v6-c-menu__content">
                      <ul class="pf-v6-c-menu__list" role="menu">
                        <li
                          class="pf-v6-c-menu__list-item pf-m-drill-up"
                          role="none"
                        >
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-toggle-icon">
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
                                    d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                                  />
                                </svg>
                              </span>
                              <span class="pf-v6-c-menu__item-text">RBAC</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Reports</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Policies</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Systems</span>
                            </span>
                          </button>
                        </li>
                      </ul>
                    </div>
                  </div>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span
                        class="pf-v6-c-menu__item-text"
                      >Thing with a longer label</span>
                    </span>
                  </button>
                </li>
              </ul>
            </div>
          </div>
        </li>
        <li class="pf-v6-c-menu__list-item" role="none">
          <button
            class="pf-v6-c-menu__item"
            type="button"
            role="menuitem"
            aria-expanded="false"
          >
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">Configuration</span>
              <span class="pf-v6-c-menu__item-toggle-icon">
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
                    d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                  />
                </svg>
              </span>
            </span>
          </button>
          <div class="pf-v6-c-menu">
            <div class="pf-v6-c-menu__content">
              <ul class="pf-v6-c-menu__list" role="menu">
                <li class="pf-v6-c-menu__list-item pf-m-drill-up" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-toggle-icon">
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
                            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                          />
                        </svg>
                      </span>
                      <span class="pf-v6-c-menu__item-text">Configuration</span>
                    </span>
                  </button>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                    aria-expanded="false"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-text">Profile</span>
                      <span class="pf-v6-c-menu__item-toggle-icon">
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
                            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                          />
                        </svg>
                      </span>
                    </span>
                  </button>
                  <div class="pf-v6-c-menu">
                    <div class="pf-v6-c-menu__content">
                      <ul class="pf-v6-c-menu__list" role="menu">
                        <li
                          class="pf-v6-c-menu__list-item pf-m-drill-up"
                          role="none"
                        >
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-toggle-icon">
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
                                    d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                                  />
                                </svg>
                              </span>
                              <span class="pf-v6-c-menu__item-text">Profile</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Avatar</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Name</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-text">Title</span>
                            </span>
                          </button>
                        </li>
                      </ul>
                    </div>
                  </div>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-text">Time zone</span>
                    </span>
                  </button>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-text">Account settings</span>
                    </span>
                  </button>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span
                        class="pf-v6-c-menu__item-text"
                      >Thing with a longer label</span>
                    </span>
                  </button>
                </li>
                <li class="pf-v6-c-menu__list-item" role="none">
                  <button
                    class="pf-v6-c-menu__item"
                    type="button"
                    role="menuitem"
                    aria-expanded="false"
                  >
                    <span class="pf-v6-c-menu__item-main">
                      <span class="pf-v6-c-menu__item-text">Edit access settings</span>
                      <span class="pf-v6-c-menu__item-toggle-icon">
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
                            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                          />
                        </svg>
                      </span>
                    </span>
                  </button>
                  <div class="pf-v6-c-menu">
                    <div class="pf-v6-c-menu__content">
                      <ul class="pf-v6-c-menu__list" role="menu">
                        <li
                          class="pf-v6-c-menu__list-item pf-m-drill-up"
                          role="none"
                        >
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span class="pf-v6-c-menu__item-toggle-icon">
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
                                    d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                                  />
                                </svg>
                              </span>
                              <span
                                class="pf-v6-c-menu__item-text"
                              >Edit access settings</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span
                                class="pf-v6-c-menu__item-text"
                              >Global access</span>
                            </span>
                          </button>
                        </li>
                        <li class="pf-v6-c-menu__list-item" role="none">
                          <button
                            class="pf-v6-c-menu__item"
                            type="button"
                            role="menuitem"
                          >
                            <span class="pf-v6-c-menu__item-main">
                              <span
                                class="pf-v6-c-menu__item-text"
                              >Account access</span>
                            </span>
                          </button>
                        </li>
                      </ul>
                    </div>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</nav>

```

### Nav item icons

```html
<nav class="pf-v6-c-nav" aria-label="Global">
  <ul class="pf-v6-c-nav__list" role="list">
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M12.5 12h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5v7c0 .827.673 1.5 1.5 1.5Zm.5-8h6v6h-6V4ZM5.5 25h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5v7c0 .827.673 1.5 1.5 1.5Zm.5-8h6v6H6v-6Zm24 12a1 1 0 0 1-1 1H3a1 1 0 0 1 0-2h26a1 1 0 0 1 1 1ZM18 16.5v7c0 .827.673 1.5 1.5 1.5h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5Zm2 .5h6v6h-6v-6Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-nav__link-text">Link 1</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link pf-m-current" aria-current="page">
        <span class="pf-v6-c-nav__link-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M29.5 8H17.81l-.681-3.208A1 1 0 0 0 16.15 4h-9.3a1 1 0 0 0-.979.792L5.19 8H2.5C1.673 8 1 8.673 1 9.5v17c0 .827.673 1.5 1.5 1.5h27c.827 0 1.5-.673 1.5-1.5v-17c0-.827-.673-1.5-1.5-1.5ZM29 26H3V10h3a1 1 0 0 0 .979-.792L7.66 6h7.682l.681 3.208a1 1 0 0 0 .979.792h12v16Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-nav__link-text">Current link</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M26.996 14.228c.003-.077.004-.153.004-.228 0-4.962-4.037-9-9-9-3.899 0-7.333 2.532-8.54 6.156A6.891 6.891 0 0 0 8 11c-3.859 0-7 3.14-7 7s3.141 7 7 7h17.5c3.032 0 5.5-2.467 5.5-5.5a5.456 5.456 0 0 0-4.004-5.272ZM25.5 23H8c-2.757 0-5-2.243-5-5s2.243-5 5-5a4.97 4.97 0 0 1 1.799.34 1.003 1.003 0 0 0 1.341-.735C11.796 9.357 14.682 7 18 7c3.859 0 7 3.14 7 7 0 .311-.028.615-.067.916a1.004 1.004 0 0 0 .898 1.123 3.473 3.473 0 0 1 3.17 3.461c0 1.93-1.57 3.5-3.5 3.5Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-nav__link-text">Link 3</span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link">
        <span class="pf-v6-c-nav__link-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M9.707 9.707 3.414 16l6.293 6.293a.999.999 0 1 1-1.414 1.414l-6.646-6.646a1.501 1.501 0 0 1 0-2.121l6.646-6.646a.999.999 0 1 1 1.414 1.414Zm20.647 5.232-6.646-6.646a.999.999 0 1 0-1.414 1.414L28.587 16l-6.293 6.293a.999.999 0 1 0 1.414 1.414l6.646-6.646a1.501 1.501 0 0 0 0-2.121ZM18.121 6.022a.997.997 0 0 0-1.186.77l-3.826 18a1 1 0 1 0 1.956.416l3.826-18a1 1 0 0 0-.77-1.186Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-nav__link-text">Link 4</span>
      </a>
    </li>
  </ul>
</nav>

```

### Docked nav

```html isBeta
<nav class="pf-v6-c-nav pf-m-docked" aria-label="Global">
  <ul class="pf-v6-c-nav__list" role="list">
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link" aria-label="Cubes">
        <span class="pf-v6-c-nav__link-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M12.5 12h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5v7c0 .827.673 1.5 1.5 1.5Zm.5-8h6v6h-6V4ZM5.5 25h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5v7c0 .827.673 1.5 1.5 1.5Zm.5-8h6v6H6v-6Zm24 12a1 1 0 0 1-1 1H3a1 1 0 0 1 0-2h26a1 1 0 0 1 1 1ZM18 16.5v7c0 .827.673 1.5 1.5 1.5h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5Zm2 .5h6v6h-6v-6Z"
            />
          </svg>
        </span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a
        href="#"
        class="pf-v6-c-nav__link pf-m-current"
        aria-current="page"
        aria-label="Folder"
      >
        <span class="pf-v6-c-nav__link-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M29.5 8H17.81l-.681-3.208A1 1 0 0 0 16.15 4h-9.3a1 1 0 0 0-.979.792L5.19 8H2.5C1.673 8 1 8.673 1 9.5v17c0 .827.673 1.5 1.5 1.5h27c.827 0 1.5-.673 1.5-1.5v-17c0-.827-.673-1.5-1.5-1.5ZM29 26H3V10h3a1 1 0 0 0 .979-.792L7.66 6h7.682l.681 3.208a1 1 0 0 0 .979.792h12v16Z"
            />
          </svg>
        </span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link" aria-label="Cloud">
        <span class="pf-v6-c-nav__link-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M26.996 14.228c.003-.077.004-.153.004-.228 0-4.962-4.037-9-9-9-3.899 0-7.333 2.532-8.54 6.156A6.891 6.891 0 0 0 8 11c-3.859 0-7 3.14-7 7s3.141 7 7 7h17.5c3.032 0 5.5-2.467 5.5-5.5a5.456 5.456 0 0 0-4.004-5.272ZM25.5 23H8c-2.757 0-5-2.243-5-5s2.243-5 5-5a4.97 4.97 0 0 1 1.799.34 1.003 1.003 0 0 0 1.341-.735C11.796 9.357 14.682 7 18 7c3.859 0 7 3.14 7 7 0 .311-.028.615-.067.916a1.004 1.004 0 0 0 .898 1.123 3.473 3.473 0 0 1 3.17 3.461c0 1.93-1.57 3.5-3.5 3.5Z"
            />
          </svg>
        </span>
      </a>
    </li>
    <li class="pf-v6-c-nav__item">
      <a href="#" class="pf-v6-c-nav__link" aria-label="Code">
        <span class="pf-v6-c-nav__link-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M9.707 9.707 3.414 16l6.293 6.293a.999.999 0 1 1-1.414 1.414l-6.646-6.646a1.501 1.501 0 0 1 0-2.121l6.646-6.646a.999.999 0 1 1 1.414 1.414Zm20.647 5.232-6.646-6.646a.999.999 0 1 0-1.414 1.414L28.587 16l-6.293 6.293a.999.999 0 1 0 1.414 1.414l6.646-6.646a1.501 1.501 0 0 0 0-2.121ZM18.121 6.022a.997.997 0 0 0-1.186.77l-3.826 18a1 1 0 1 0 1.956.416l3.826-18a1 1 0 0 0-.77-1.186Z"
            />
          </svg>
        </span>
      </a>
    </li>
  </ul>
</nav>

```

## Documentation

### Overview

The navigation system relies on several different sub-components:

* `.pf-v6-c-nav__list` - default navigation list. It is the basis for both default and expandable, vertical navigation.

### Accessibility

| Attribute | Applied to | Outcome |
| -- | -- | -- |
| `aria-label="[landmark description]"` | `.pf-v6-c-nav` |  Describes `<nav>` landmark. |
| `aria-label="[section title]"` | `.pf-v6-c-nav__section` |  Describes a nav `<section>`, where a `.pf-v6-c-nav__section-title` is not present. |
| `aria-labelledby="[id value of link describing subnav]"` | `.pf-v6-c-nav__subnav` |  Gives the subnav `<section>` landmark an accessible name by referring to the element that provides the subnav `<section>` landmark title. |
| `aria-expanded="false"` | `.pf-v6-c-nav__link` |  Indicates that subnav section is hidden. |
| `aria-expanded="true"` | `.pf-v6-c-nav__link` |  Indicates that subnav section is visible. |
| `hidden` | `.pf-v6-c-nav__subnav` |  Indicates that the subnav section is hidden so that it isn't visible in the UI and isn't accessed by assistive technologies. |
| `disabled` | `.pf-v6-c-nav__scroll-button` | Indicates that a scroll button is disabled, when at the first or last item of a list. **Required when disabled** |
| `aria-current="page"` | `.pf-v6-c-nav__link` |  Indicates the current page link. Can only occur once on page. |
| `aria-haspopup="true"` | `.pf-v6-c-nav__link` | Declares that a nav item has a submenu. |

### Usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-nav` | `<nav>` | Initiates a primary nav element. |
| `.pf-v6-c-nav__subnav` | `<section>` | Initiates a subnav section. |
| `.pf-v6-c-nav__list` | `<ul>` | Initiates nav list. |
| `.pf-v6-c-nav__item` | `<li>` | Initiates nav list item. |
| `.pf-v6-c-nav__link` | `<a>` | Initiates nav list link. |
| `.pf-v6-c-nav__link-icon` | `<span>` | Initiates nav list link icon. |
| `.pf-v6-c-nav__link-text` | `<span>` | Initiates nav list link text. |
| `.pf-v6-c-nav__section` | `<section>` | Initiates a nav section element. |
| `.pf-v6-c-nav__section-title` | `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>` | Initiates a nav section title. |
| `.pf-v6-c-nav__toggle` | `<span>` | Initiates the nav toggle wrapper. |
| `.pf-v6-c-nav__toggle-icon` | `<span>` | Initiates a nav toggle icon wrapper. |
| `.pf-v6-c-nav__scroll-button` | `<button>` | Initiates a nav scroll button. **Required for horizontal navs** |
| `.pf-m-horizontal` | `.pf-v6-c-nav` | Modifies nav for the horizontal variation. |
| `.pf-m-horizontal-subnav` | `.pf-v6-c-nav` | Modifies nav for the horizontal subnav variation. |
| `.pf-m-docked` | `.pf-v6-c-nav` | Modifies nav for the docked variation. |
| `.pf-m-flyout` | `.pf-v6-c-nav__item` | Modifies nav item for the flyout variation. |
| `.pf-m-scrollable` | `.pf-v6-c-nav` | Modifies nav for the scrollable state. |
| `.pf-m-expanded` | `.pf-v6-c-nav__item` | Modifies for the expanded state. |
| `.pf-m-current` | `.pf-v6-c-nav__link` | Modifies for the current state. |
| `.pf-m-hover` | `.pf-v6-c-nav__link` | Modifies for the hover state. |
