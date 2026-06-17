---
id: 'Dashboard'
section: patterns
cssPrefix: pf-d-dashboard
---## Examples

### Basic

```html isFullscreen
<div class="pf-v6-c-page" id="dashboard-demo">
  <div class="pf-v6-c-skip-to-content">
    <a class="pf-v6-c-button pf-m-primary" href="#main-content-dashboard-demo">
      <span class="pf-v6-c-button__text">Skip to content</span>
    </a>
  </div>

  <header class="pf-v6-c-masthead" id="dashboard-demo-docked">
    <div class="pf-v6-c-masthead__main">
      <span class="pf-v6-c-masthead__toggle">
        <button
          class="pf-v6-c-button pf-m-hamburger pf-m-plain"
          type="button"
          aria-label="Global navigation"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              viewBox="0 0 10 10"
              class="pf-v6-c-button--hamburger-icon pf-v6-svg"
              width="1em"
              height="1em"
            >
              <path class="pf-v6-c-button--hamburger-icon--top" d="M1,1 L9,1" />
              <path
                class="pf-v6-c-button--hamburger-icon--middle"
                d="M1,5 L9,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--arrow"
                d="M1,5 L1,5 L1,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--bottom"
                d="M9,9 L1,9"
              />
            </svg>
          </span>
        </button>
      </span>
      <div class="pf-v6-c-masthead__brand">
        <a class="pf-v6-c-masthead__logo" href="#">
          <svg height="37px" viewBox="0 0 679 158">
            <title>PatternFly</title>
            <defs>
              <linearGradient
                x1="68%"
                y1="2.25860997e-13%"
                x2="32%"
                y2="100%"
                id="linearGradient-dashboard-demo-docked"
              >
                <stop stop-color="#2B9AF3" offset="0%" />
                <stop
                  stop-color="#73BCF7"
                  stop-opacity="0.502212631"
                  offset="100%"
                />
              </linearGradient>
            </defs>
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <g
                transform="translate(206.000000, 45.750000)"
                fill="var(--pf-t--global--text--color--regular)"
                fill-rule="nonzero"
              >
                <path
                  d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                />
                <path
                  d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                />
                <path
                  d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                />
                <path
                  d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                />
                <path
                  d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                />
                <path
                  d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                />
                <path
                  d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                />
                <polygon
                  points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                />
                <polygon
                  points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                />
                <path
                  d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                />
              </g>
              <g transform="translate(0.000000, 0.000000)">
                <path
                  d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                  fill="#0066CC"
                />
                <path
                  d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                  fill="url(#linearGradient-dashboard-demo-docked)"
                />
                <path
                  d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                  fill="url(#linearGradient-dashboard-demo-docked)"
                  transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                />
              </g>
            </g>
          </svg>
        </a>
      </div>
    </div>
    <div class="pf-v6-c-masthead__content">
      <div
        class="pf-v6-c-toolbar pf-m-static"
        id="dashboard-demo-docked-toolbar"
      >
        <div class="pf-v6-c-toolbar__content">
          <div class="pf-v6-c-toolbar__content-section">
            <div
              class="pf-v6-c-toolbar__group pf-m-align-end pf-m-spacer-none pf-m-spacer-md-on-md pf-m-action-group-plain"
            >
              <div
                class="pf-v6-c-toolbar__group pf-m-hidden pf-m-visible-on-lg pf-m-action-group-plain"
              >
                <div class="pf-v6-c-toolbar__item">
                  <button
                    class="pf-v6-c-menu-toggle pf-m-plain"
                    type="button"
                    aria-expanded="false"
                    aria-label="Application launcher"
                  >
                    <span class="pf-v6-c-menu-toggle__icon">
                      <svg
                        class="pf-v6-svg"
                        viewBox="0 0 512 512"
                        fill="currentColor"
                        aria-hidden="true"
                        role="img"
                        width="1em"
                        height="1em"
                      >
                        <path
                          d="M149.333 56v80c0 13.255-10.745 24-24 24H24c-13.255 0-24-10.745-24-24V56c0-13.255 10.745-24 24-24h101.333c13.255 0 24 10.745 24 24zm181.334 240v-80c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24h101.333c13.256 0 24.001-10.745 24.001-24zm32-240v80c0 13.255 10.745 24 24 24H488c13.255 0 24-10.745 24-24V56c0-13.255-10.745-24-24-24H386.667c-13.255 0-24 10.745-24 24zm-32 80V56c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24h101.333c13.256 0 24.001-10.745 24.001-24zm-205.334 56H24c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24zM0 376v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H24c-13.255 0-24 10.745-24 24zm386.667-56H488c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H386.667c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24zm0 160H488c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H386.667c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24zM181.333 376v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
                <div class="pf-v6-c-toolbar__item">
                  <button
                    class="pf-v6-c-menu-toggle pf-m-settings pf-m-plain"
                    type="button"
                    aria-expanded="false"
                    aria-label="Settings"
                  >
                    <span class="pf-v6-c-menu-toggle__icon">
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
                          d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
                <div class="pf-v6-c-toolbar__item">
                  <button
                    class="pf-v6-c-menu-toggle pf-m-plain"
                    type="button"
                    aria-expanded="false"
                    aria-label="Help"
                  >
                    <span class="pf-v6-c-menu-toggle__icon">
                      <svg
                        class="pf-v6-svg"
                        viewBox="0 0 512 512"
                        fill="currentColor"
                        aria-hidden="true"
                        role="img"
                        width="1em"
                        height="1em"
                      >
                        <path
                          d="M504 256c0 136.997-111.043 248-248 248S8 392.997 8 256C8 119.083 119.043 8 256 8s248 111.083 248 248zM262.655 90c-54.497 0-89.255 22.957-116.549 63.758-3.536 5.286-2.353 12.415 2.715 16.258l34.699 26.31c5.205 3.947 12.621 3.008 16.665-2.122 17.864-22.658 30.113-35.797 57.303-35.797 20.429 0 45.698 13.148 45.698 32.958 0 14.976-12.363 22.667-32.534 33.976C247.128 238.528 216 254.941 216 296v4c0 6.627 5.373 12 12 12h56c6.627 0 12-5.373 12-12v-1.333c0-28.462 83.186-29.647 83.186-106.667 0-58.002-60.165-102-116.531-102zM256 338c-25.365 0-46 20.635-46 46 0 25.364 20.635 46 46 46s46-20.636 46-46c0-25.365-20.635-46-46-46z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
              </div>

              <div class="pf-v6-c-toolbar__item pf-m-hidden-on-lg">
                <button
                  class="pf-v6-c-menu-toggle pf-m-plain"
                  type="button"
                  aria-expanded="false"
                  aria-label="Actions"
                >
                  <span class="pf-v6-c-menu-toggle__icon">
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
                        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
  <div class="pf-v6-c-page__sidebar">
    <div class="pf-v6-c-page__sidebar-main">
      <div class="pf-v6-c-page__sidebar-body">
        <nav
          class="pf-v6-c-nav"
          id="dashboard-demo-primary-nav"
          aria-label="Global"
        >
          <ul class="pf-v6-c-nav__list" role="list">
            <li class="pf-v6-c-nav__item">
              <a href="#" class="pf-v6-c-nav__link">
                <span class="pf-v6-c-nav__link-text">System panel</span>
              </a>
            </li>
            <li class="pf-v6-c-nav__item">
              <a
                href="#"
                class="pf-v6-c-nav__link pf-m-current"
                aria-current="page"
              >
                <span class="pf-v6-c-nav__link-text">Policy</span>
              </a>
            </li>
            <li class="pf-v6-c-nav__item">
              <a href="#" class="pf-v6-c-nav__link">
                <span class="pf-v6-c-nav__link-text">Authentication</span>
              </a>
            </li>
            <li class="pf-v6-c-nav__item">
              <a href="#" class="pf-v6-c-nav__link">
                <span class="pf-v6-c-nav__link-text">Network services</span>
              </a>
            </li>
            <li class="pf-v6-c-nav__item">
              <a href="#" class="pf-v6-c-nav__link">
                <span class="pf-v6-c-nav__link-text">Server</span>
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </div>
  <div class="pf-v6-c-page__main-container" tabindex="-1">
    <main
      class="pf-v6-c-page__main"
      tabindex="-1"
      id="main-content-dashboard-demo"
    >
      <section class="pf-v6-c-page__main-breadcrumb pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <nav class="pf-v6-c-breadcrumb" aria-label="breadcrumb">
            <ol class="pf-v6-c-breadcrumb__list" role="list">
              <li class="pf-v6-c-breadcrumb__item">
                <a href="#" class="pf-v6-c-breadcrumb__link">Section home</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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

                <a
                  href="#"
                  class="pf-v6-c-breadcrumb__link pf-m-current"
                  aria-current="page"
                >Section landing</a>
              </li>
            </ol>
          </nav>
        </div>
      </section>
      <section
        class="pf-v6-c-page__main-section pf-m-limit-width"
        aria-labelledby="main-title"
      >
        <div class="pf-v6-c-page__main-body">
          <h1
            class="pf-v6-c-content--h1 pf-m-page-title"
            id="main-title"
          >Main title</h1>
          <p class="pf-v6-c-content--p">This is a full page demo.</p>
        </div>
      </section>
      <section class="pf-v6-c-page__main-section pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <div class="pf-v6-l-grid pf-m-gutter">
            <div class="pf-v6-c-card pf-m-expanded">
              <div class="pf-v6-c-card__header">
                <div class="pf-v6-c-card__header-toggle">
                  <button
                    class="pf-v6-c-button pf-m-plain"
                    id="dashboard-demo-expandable-status-card-1-toggle"
                    type="button"
                    aria-labelledby="dashboard-demo-expandable-status-card-1-title dashboard-demo-expandable-status-card-1-toggle"
                    aria-label="Details"
                  >
                    <span class="pf-v6-c-button__icon pf-m-start">
                      <span class="pf-v6-c-card__header-toggle-icon">
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
                </div>
                <div class="pf-v6-c-card__actions">
                  <button
                    class="pf-v6-c-menu-toggle pf-m-plain"
                    type="button"
                    aria-expanded="false"
                    aria-label="Menu toggle"
                    id="dashboard-demo-expandable-status-card-1-action-kebab"
                  >
                    <span class="pf-v6-c-menu-toggle__icon">
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
                          d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
                <div
                  class="pf-v6-c-card__title"
                  id="dashboard-demo-expandable-status-card-1-title"
                >
                  <h2 class="pf-v6-c-title pf-m-xl">Improve recommended pathways</h2>
                </div>
              </div>
              <div class="pf-v6-c-card__expandable-content">
                <div class="pf-v6-l-flex pf-m-column pf-m-row-on-md">
                  <div
                    class="pf-v6-l-flex pf-m-flex-1 pf-m-align-self-stretch pf-m-align-items-stretch"
                  >
                    <div class="pf-v6-c-card pf-m-plain">
                      <div class="pf-v6-c-card__body">
                        <div
                          class="pf-v6-l-flex pf-m-column pf-v6-u-h-100 pf-m-space-items-sm"
                        >
                          <div
                            class="pf-v6-l-flex pf-m-space-items-sm pf-m-column-on-md pf-m-row-on-lg pf-m-spacer-md-on-md pf-m-spacer-sm-on-lg"
                          >
                            <div class="pf-v6-c-label-group">
                              <div class="pf-v6-c-label-group__main">
                                <ul
                                  class="pf-v6-c-label-group__list"
                                  role="list"
                                  aria-label="Group of labels"
                                >
                                  <li class="pf-v6-c-label-group__list-item">
                                    <span
                                      class="pf-v6-c-label pf-m-outline pf-m-blue"
                                    >
                                      <span class="pf-v6-c-label__content">
                                        <span class="pf-v6-c-label__icon">
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
                                              d="M23 23.917a1.62 1.62 0 0 1-1.149-.475L9 10.59l-6.204 6.205a1.127 1.127 0 0 1-1.592-1.592L7.85 8.557a1.629 1.629 0 0 1 2.299 0L23 21.409l6.204-6.205a1.127 1.127 0 0 1 1.592 1.592l-6.646 6.646a1.624 1.624 0 0 1-1.149.475Z"
                                            />
                                          </svg>
                                        </span>
                                        <span
                                          class="pf-v6-c-label__text"
                                        >Performance</span>
                                      </span>
                                    </span>
                                  </li>
                                </ul>
                              </div>
                            </div>
                            <a href="#">378 systems</a>
                          </div>
                          <div class="pf-v6-l-flex__item pf-m-spacer-md">
                            <p>Upgrade your kernel version to remediate ntpd time sync issues, kernel panics, network instabilities and issues with system performance</p>
                          </div>
                          <div
                            class="pf-v6-l-flex pf-m-grow pf-m-column pf-m-row-on-lg pf-m-justify-content-flex-end pf-m-justify-content-flex-start-on-lg pf-m-align-content-flex-end-on-lg"
                            style="row-gap: var(--pf-6-global--spacer--md);"
                          >
                            <div
                              class="pf-v6-l-flex__item"
                              style="margin-block-end: -.25em"
                            >
                              <span class="pf-v6-c-label pf-m-red">
                                <span class="pf-v6-c-label__content">
                                  <span class="pf-v6-c-label__text">Incident</span>
                                </span>
                              </span>
                            </div>
                            <div
                              class="pf-v6-l-flex pf-m-space-items-sm pf-m-align-items-center pf-m-nowrap"
                              style="row-gap: var(--pf-6-global--spacer--md);"
                            >
                              <span class="pf-v6-c-icon">
                                <span
                                  class="pf-v6-c-icon__content pf-m-success"
                                >
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
                                      d="M19 16c0 1.654-1.346 3-3 3s-3-1.346-3-3 1.346-3 3-3 3 1.346 3 3ZM3 16c0-3.472 1.353-6.737 3.808-9.192a.999.999 0 1 0-1.414-1.414C2.561 8.227 1 11.994 1 16s1.561 7.773 4.394 10.606a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414A12.918 12.918 0 0 1 3 16ZM26.606 5.394a.999.999 0 1 0-1.414 1.414C27.647 9.264 29 12.528 29 16s-1.353 6.737-3.808 9.192a.999.999 0 1 0 1.414 1.414C29.439 23.773 31 20.006 31 16s-1.561-7.773-4.394-10.606ZM11.05 9.636a.999.999 0 0 0-1.414 0c-3.509 3.509-3.509 9.219 0 12.728a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414 7.008 7.008 0 0 1 0-9.899.999.999 0 0 0 0-1.414Zm11.314 0a.999.999 0 1 0-1.414 1.414 7.008 7.008 0 0 1 0 9.899.999.999 0 1 0 1.414 1.414c3.509-3.509 3.509-9.219 0-12.728Z"
                                    />
                                  </svg>
                                </span>
                              </span>
                              <p class="pf-v6-u-color-200">
                                System reboot
                                <b class="pf-v6-u-color-100">is not</b> required
                              </p>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__footer">
                        <a
                          class="pf-v6-c-button pf-m-inline pf-m-link"
                          href="#"
                        >
                          <span class="pf-v6-c-button__text">View pathway</span>
                          <span class="pf-v6-c-button__icon pf-m-end">
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
                                d="M190.5 66.9l22.2-22.2c9.4-9.4 24.6-9.4 33.9 0L441 239c9.4 9.4 9.4 24.6 0 33.9L246.6 467.3c-9.4 9.4-24.6 9.4-33.9 0l-22.2-22.2c-9.5-9.5-9.3-25 .4-34.3L311.4 296H24c-13.3 0-24-10.7-24-24v-32c0-13.3 10.7-24 24-24h287.4L190.9 101.2c-9.8-9.3-10-24.8-.4-34.3z"
                              />
                            </svg>
                          </span>
                        </a>
                      </div>
                    </div>
                  </div>
                  <hr
                    class="pf-v6-c-divider pf-m-vertical-on-md pf-m-inset-3xl"
                  />
                  <div
                    class="pf-v6-l-flex pf-m-flex-1 pf-m-align-self-stretch pf-m-align-items-stretch"
                  >
                    <div class="pf-v6-c-card pf-m-plain">
                      <div class="pf-v6-c-card__body">
                        <div
                          class="pf-v6-l-flex pf-m-column pf-v6-u-h-100 pf-m-space-items-sm"
                        >
                          <div
                            class="pf-v6-l-flex pf-m-space-items-sm pf-m-column-on-md pf-m-row-on-lg pf-m-spacer-md-on-md pf-m-spacer-sm-on-lg"
                          >
                            <div class="pf-v6-c-label-group">
                              <div class="pf-v6-c-label-group__main">
                                <ul
                                  class="pf-v6-c-label-group__list"
                                  role="list"
                                  aria-label="Group of labels"
                                >
                                  <li class="pf-v6-c-label-group__list-item">
                                    <span
                                      class="pf-v6-c-label pf-m-outline pf-m-blue"
                                    >
                                      <span class="pf-v6-c-label__content">
                                        <span class="pf-v6-c-label__icon">
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
                                              d="M16 30.856a1 1 0 0 1-.5-.134l-12-6.929a1 1 0 0 1-.5-.866V9.072c0-.357.19-.688.5-.866l12-6.929a1.003 1.003 0 0 1 1 0l12 6.929a1 1 0 0 1 .5.866v13.855c0 .357-.19.688-.5.866l-12 6.929a1 1 0 0 1-.5.134ZM5 22.351l11 6.352 11-6.352V9.65L16 3.298 5 9.65v12.701Zm23 .577h.01H28Z"
                                            />
                                          </svg>
                                        </span>
                                        <span
                                          class="pf-v6-c-label__text"
                                        >Stablility</span>
                                      </span>
                                    </span>
                                  </li>
                                  <li class="pf-v6-c-label-group__list-item">
                                    <button
                                      class="pf-v6-c-label pf-m-overflow"
                                      type="button"
                                    >
                                      <span class="pf-v6-c-label__content">
                                        <span class="pf-v6-c-label__text">1 more</span>
                                      </span>
                                    </button>
                                  </li>
                                </ul>
                              </div>
                            </div>
                            <a href="#">211 systems</a>
                          </div>
                          <div class="pf-v6-l-flex__item pf-m-spacer-md">
                            <p>Adjust your networking configuration to get ahead of network perfomance degradations and packet losses</p>
                          </div>
                          <div
                            class="pf-v6-l-flex pf-m-grow pf-m-column pf-m-row-on-lg pf-m-justify-content-flex-end pf-m-justify-content-flex-start-on-lg pf-m-align-content-flex-end-on-lg"
                            style="row-gap: var(--pf-6-global--spacer--md);"
                          >
                            <div
                              class="pf-v6-l-flex pf-m-space-items-sm pf-m-align-items-center pf-m-nowrap"
                              style="row-gap: var(--pf-6-global--spacer--md);"
                            >
                              <span class="pf-v6-c-icon">
                                <span class="pf-v6-c-icon__content pf-m-danger">
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
                                      d="M19 16c0 1.654-1.346 3-3 3s-3-1.346-3-3 1.346-3 3-3 3 1.346 3 3ZM3 16c0-3.472 1.353-6.737 3.808-9.192a.999.999 0 1 0-1.414-1.414C2.561 8.227 1 11.994 1 16s1.561 7.773 4.394 10.606a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414A12.918 12.918 0 0 1 3 16ZM26.606 5.394a.999.999 0 1 0-1.414 1.414C27.647 9.264 29 12.528 29 16s-1.353 6.737-3.808 9.192a.999.999 0 1 0 1.414 1.414C29.439 23.773 31 20.006 31 16s-1.561-7.773-4.394-10.606ZM11.05 9.636a.999.999 0 0 0-1.414 0c-3.509 3.509-3.509 9.219 0 12.728a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414 7.008 7.008 0 0 1 0-9.899.999.999 0 0 0 0-1.414Zm11.314 0a.999.999 0 1 0-1.414 1.414 7.008 7.008 0 0 1 0 9.899.999.999 0 1 0 1.414 1.414c3.509-3.509 3.509-9.219 0-12.728Z"
                                    />
                                  </svg>
                                </span>
                              </span>
                              <p class="pf-v6-u-color-200">
                                System reboot
                                <b class="pf-v6-u-color-100">is</b> required
                              </p>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__footer">
                        <a
                          class="pf-v6-c-button pf-m-inline pf-m-link"
                          href="#"
                        >
                          <span class="pf-v6-c-button__text">View pathway</span>
                          <span class="pf-v6-c-button__icon pf-m-end">
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
                                d="M190.5 66.9l22.2-22.2c9.4-9.4 24.6-9.4 33.9 0L441 239c9.4 9.4 9.4 24.6 0 33.9L246.6 467.3c-9.4 9.4-24.6 9.4-33.9 0l-22.2-22.2c-9.5-9.5-9.3-25 .4-34.3L311.4 296H24c-13.3 0-24-10.7-24-24v-32c0-13.3 10.7-24 24-24h287.4L190.9 101.2c-9.8-9.3-10-24.8-.4-34.3z"
                              />
                            </svg>
                          </span>
                        </a>
                      </div>
                    </div>
                  </div>
                  <hr
                    class="pf-v6-c-divider pf-m-vertical-on-md pf-m-inset-3xl"
                  />
                  <div
                    class="pf-v6-l-flex pf-m-flex-1 pf-m-align-self-stretch pf-m-align-items-stretch"
                  >
                    <div class="pf-v6-c-card pf-m-plain">
                      <div class="pf-v6-c-card__body">
                        <div
                          class="pf-v6-l-flex pf-m-column pf-v6-u-h-100 pf-m-space-items-sm"
                        >
                          <div
                            class="pf-v6-l-flex pf-m-space-items-sm pf-m-column-on-md pf-m-row-on-lg pf-m-spacer-md-on-md pf-m-spacer-sm-on-lg"
                          >
                            <div class="pf-v6-c-label-group">
                              <div class="pf-v6-c-label-group__main">
                                <ul
                                  class="pf-v6-c-label-group__list"
                                  role="list"
                                  aria-label="Group of labels"
                                >
                                  <li class="pf-v6-c-label-group__list-item">
                                    <span
                                      class="pf-v6-c-label pf-m-outline pf-m-blue"
                                    >
                                      <span class="pf-v6-c-label__content">
                                        <span class="pf-v6-c-label__icon">
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
                                              d="M22 17v3.5c0 .827-.673 1.5-1.5 1.5H17a1 1 0 1 1 0-2h1.596l-3.302-3.292s-3.186-3.174-4.109-4.098c-.905-.906-2.109-1.404-3.39-1.404s-2.485.498-3.391 1.404C3.499 13.515 3 14.719 3 16s.499 2.484 1.404 3.39c.905.906 2.109 1.404 3.391 1.404s2.484-.498 3.39-1.404l1.109-1.107a.999.999 0 1 1 1.412 1.416l-1.107 1.105c-1.283 1.284-2.989 1.99-4.804 1.99s-3.521-.706-4.805-1.99C1.707 19.521 1 17.815 1 16s.707-3.521 1.99-4.804c1.283-1.284 2.989-1.99 4.805-1.99s3.521.706 4.804 1.99c.924.924 4.107 4.096 4.107 4.096L20 18.576V17a1 1 0 1 1 2 0Zm7.01-5.804c-1.283-1.284-2.989-1.991-4.805-1.991s-3.521.707-4.804 1.991L18.295 12.3a.999.999 0 1 0 1.41 1.418l1.11-1.108c.905-.906 2.109-1.405 3.39-1.405s2.485.499 3.391 1.405C28.501 13.515 29 14.719 29 16s-.499 2.484-1.404 3.39a4.748 4.748 0 0 1-2.732 1.36 1 1 0 1 0 .273 1.98 6.727 6.727 0 0 0 3.873-1.927C30.293 19.52 31 17.814 31 15.999s-.707-3.521-1.99-4.804Z"
                                            />
                                          </svg>
                                        </span>
                                        <span
                                          class="pf-v6-c-label__text"
                                        >Availability</span>
                                      </span>
                                    </span>
                                  </li>
                                </ul>
                              </div>
                            </div>
                            <a href="#">166 systems</a>
                          </div>
                          <div class="pf-v6-l-flex__item pf-m-spacer-md">
                            <p>Fine tune your Oracle DB configuration to improve database performance and avoid process failure</p>
                          </div>
                          <div
                            class="pf-v6-l-flex pf-m-grow pf-m-column pf-m-row-on-lg pf-m-justify-content-flex-end pf-m-justify-content-flex-start-on-lg pf-m-align-content-flex-end-on-lg"
                            style="row-gap: var(--pf-6-global--spacer--md);"
                          >
                            <div
                              class="pf-v6-l-flex__item"
                              style="margin-block-end: -.25em"
                            >
                              <span class="pf-v6-c-label pf-m-red">
                                <span class="pf-v6-c-label__content">
                                  <span class="pf-v6-c-label__text">Incident</span>
                                </span>
                              </span>
                            </div>
                            <div
                              class="pf-v6-l-flex pf-m-space-items-sm pf-m-align-items-center pf-m-nowrap"
                              style="row-gap: var(--pf-6-global--spacer--md);"
                            >
                              <span class="pf-v6-c-icon">
                                <span
                                  class="pf-v6-c-icon__content pf-m-success"
                                >
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
                                      d="M19 16c0 1.654-1.346 3-3 3s-3-1.346-3-3 1.346-3 3-3 3 1.346 3 3ZM3 16c0-3.472 1.353-6.737 3.808-9.192a.999.999 0 1 0-1.414-1.414C2.561 8.227 1 11.994 1 16s1.561 7.773 4.394 10.606a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414A12.918 12.918 0 0 1 3 16ZM26.606 5.394a.999.999 0 1 0-1.414 1.414C27.647 9.264 29 12.528 29 16s-1.353 6.737-3.808 9.192a.999.999 0 1 0 1.414 1.414C29.439 23.773 31 20.006 31 16s-1.561-7.773-4.394-10.606ZM11.05 9.636a.999.999 0 0 0-1.414 0c-3.509 3.509-3.509 9.219 0 12.728a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414 7.008 7.008 0 0 1 0-9.899.999.999 0 0 0 0-1.414Zm11.314 0a.999.999 0 1 0-1.414 1.414 7.008 7.008 0 0 1 0 9.899.999.999 0 1 0 1.414 1.414c3.509-3.509 3.509-9.219 0-12.728Z"
                                    />
                                  </svg>
                                </span>
                              </span>
                              <p class="pf-v6-u-color-200">
                                System reboot
                                <b class="pf-v6-u-color-100">is not</b> required
                              </p>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-c-card__footer">
                        <a
                          class="pf-v6-c-button pf-m-inline pf-m-link"
                          href="#"
                        >
                          <span class="pf-v6-c-button__text">View pathway</span>
                          <span class="pf-v6-c-button__icon pf-m-end">
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
                                d="M190.5 66.9l22.2-22.2c9.4-9.4 24.6-9.4 33.9 0L441 239c9.4 9.4 9.4 24.6 0 33.9L246.6 467.3c-9.4 9.4-24.6 9.4-33.9 0l-22.2-22.2c-9.5-9.5-9.3-25 .4-34.3L311.4 296H24c-13.3 0-24-10.7-24-24v-32c0-13.3 10.7-24 24-24h287.4L190.9 101.2c-9.8-9.3-10-24.8-.4-34.3z"
                              />
                            </svg>
                          </span>
                        </a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div
              class="pf-v6-l-grid__item pf-m-gutter pf-m-4-col-on-lg pf-m-6-col-on-2xl"
              style="--pf-v6-l-grid--item--Order-on-lg:3"
            >
              <div class="pf-v6-l-flex pf-m-column">
                <div class="pf-v6-c-card" id="dashboard-demo-status-card-1">
                  <div class="pf-v6-c-card__header">
                    <h2 class="pf-v6-c-title pf-m-xl">Status</h2>
                  </div>
                  <div class="pf-v6-c-card__body">
                    <div
                      class="pf-v6-l-gallery pf-m-gutter"
                      style="--pf-v6-l-gallery--GridTemplateColumns--min: 100%; --pf-v6-l-gallery--GridTemplateColumns--min-on-sm: 180px; --pf-v6-l-gallery--GridTemplateColumns--min-on-lg: 150px; --pf-v6-l-gallery--GridTemplateColumns--max-on-sm: 1fr;"
                    >
                      <div class="pf-v6-l-flex pf-m-space-items-sm pf-m-nowrap">
                        <div class="pf-v6-l-flex__item">
                          <span class="pf-v6-c-icon">
                            <span class="pf-v6-c-icon__content pf-m-success">
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
                                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                />
                              </svg>
                            </span>
                          </span>
                        </div>
                        <div class="pf-v6-l-flex__item">
                          <span>Cluster</span>
                        </div>
                      </div>
                      <div class="pf-v6-l-flex pf-m-space-items-sm pf-m-nowrap">
                        <div class="pf-v6-l-flex__item">
                          <span class="pf-v6-c-icon">
                            <span class="pf-v6-c-icon__content pf-m-danger">
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
                                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm-1.5 8a1.5 1.5 0 1 1 3 0v7a1.5 1.5 0 1 1-3 0V9ZM16 25.001a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 25.001Z"
                                />
                              </svg>
                            </span>
                          </span>
                        </div>
                        <div class="pf-v6-l-flex__item pf-v6-u-text-nowrap">
                          <span class="popover-parent">
                            <a href="#">Control Panel</a>
                          </span>
                        </div>
                      </div>
                      <div class="pf-v6-l-flex pf-m-space-items-sm pf-m-nowrap">
                        <div class="pf-v6-l-flex__item pf-v6-u-text-nowrap">
                          <span class="pf-v6-c-icon">
                            <span class="pf-v6-c-icon__content pf-m-danger">
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
                                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm-1.5 8a1.5 1.5 0 1 1 3 0v7a1.5 1.5 0 1 1-3 0V9ZM16 25.001a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 25.001Z"
                                />
                              </svg>
                            </span>
                          </span>
                        </div>
                        <div
                          class="pf-v6-l-flex pf-m-column pf-m-space-items-none"
                        >
                          <div class="pf-v6-l-flex__item">
                            <a href="#">Operators</a>
                          </div>
                          <div class="pf-v6-l-flex__item">
                            <span class="pf-v6-u-text-color-subtle">1 degraded</span>
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-l-flex pf-m-space-items-sm pf-m-nowrap">
                        <div class="pf-v6-l-flex__item">
                          <span class="pf-v6-c-icon">
                            <span class="pf-v6-c-icon__content pf-m-success">
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
                                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                />
                              </svg>
                            </span>
                          </span>
                        </div>
                        <div
                          class="pf-v6-l-flex pf-m-column pf-m-space-items-none"
                        >
                          <div class="pf-v6-l-flex__item">
                            <a href="#">Image Vulnerabilities</a>
                          </div>
                          <div class="pf-v6-l-flex__item">
                            <span class="pf-v6-u-color-200">0 vulnerabilities</span>
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-l-flex pf-m-space-items-sm pf-m-nowrap">
                        <div class="pf-v6-l-flex__item">
                          <span class="pf-v6-c-icon">
                            <span class="pf-v6-c-icon__content pf-m-success">
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
                                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                />
                              </svg>
                            </span>
                          </span>
                        </div>
                        <div
                          class="pf-v6-l-flex pf-m-column pf-m-space-items-none"
                        >
                          <div class="pf-v6-l-flex__item">
                            <a href="#">Storage</a>
                          </div>
                          <div class="pf-v6-l-flex__item">
                            <span class="pf-v6-u-color-200">Degraded</span>
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-l-flex pf-m-space-items-sm pf-m-nowrap">
                        <div class="pf-v6-l-flex__item">
                          <span class="pf-v6-c-icon">
                            <span class="pf-v6-c-icon__content pf-m-success">
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
                                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                />
                              </svg>
                            </span>
                          </span>
                        </div>
                        <div
                          class="pf-v6-l-flex pf-m-column pf-m-space-items-none"
                        >
                          <div class="pf-v6-l-flex__item">
                            <a href="#">Hardware</a>
                          </div>
                        </div>
                      </div>
                      <div class="pf-v6-l-flex pf-m-space-items-sm pf-m-nowrap">
                        <div class="pf-v6-l-flex__item">
                          <span class="pf-v6-c-icon">
                            <span class="pf-v6-c-icon__content pf-m-success">
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
                                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                />
                              </svg>
                            </span>
                          </span>
                        </div>
                        <div
                          class="pf-v6-l-flex pf-m-column pf-m-space-items-none"
                        >
                          <div class="pf-v6-l-flex__item">
                            <a href="#">Insights</a>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <hr class="pf-v6-c-divider" />
                  <div class="pf-v6-c-notification-drawer">
                    <div class="pf-v6-c-notification-drawer__body">
                      <section class="pf-v6-c-notification-drawer__group">
                        <button
                          class="pf-v6-c-notification-drawer__group-toggle"
                          aria-expanded="false"
                        >
                          <div
                            class="pf-v6-c-notification-drawer__group-toggle-title"
                          >
                            <div class="pf-v6-l-flex">
                              <div
                                class="pf-v6-l-flex__item pf-m-spacer-md"
                              >Notifications</div>
                              <div class="pf-v6-c-label-group">
                                <div class="pf-v6-c-label-group__main">
                                  <ul
                                    class="pf-v6-c-label-group__list"
                                    role="list"
                                    aria-label="Group of labels"
                                  >
                                    <li class="pf-v6-c-label-group__list-item">
                                      <span class="pf-v6-c-label pf-m-red">
                                        <span class="pf-v6-c-label__content">
                                          <span class="pf-v6-c-label__icon">
                                            <i
                                              class="fas fa-fw fa-exclamation-circle"
                                              aria-hidden="true"
                                            ></i>
                                          </span>
                                          <span class="pf-v6-c-label__text">1</span>
                                        </span>
                                      </span>
                                    </li>
                                    <li class="pf-v6-c-label-group__list-item">
                                      <span class="pf-v6-c-label pf-m-orange">
                                        <span class="pf-v6-c-label__content">
                                          <span class="pf-v6-c-label__icon">
                                            <i
                                              class="fas fa-fw fa-exclamation-circle"
                                              aria-hidden="true"
                                            ></i>
                                          </span>
                                          <span class="pf-v6-c-label__text">1</span>
                                        </span>
                                      </span>
                                    </li>
                                    <li class="pf-v6-c-label-group__list-item">
                                      <span class="pf-v6-c-label pf-m-green">
                                        <span class="pf-v6-c-label__content">
                                          <span class="pf-v6-c-label__icon">
                                            <i
                                              class="fas fa-fw fa-check-circle"
                                              aria-hidden="true"
                                            ></i>
                                          </span>
                                          <span class="pf-v6-c-label__text">3</span>
                                        </span>
                                      </span>
                                    </li>
                                    <li class="pf-v6-c-label-group__list-item">
                                      <span class="pf-v6-c-label pf-m-blue">
                                        <span class="pf-v6-c-label__content">
                                          <span class="pf-v6-c-label__icon">
                                            <i
                                              class="fas fa-fw fa-info-circle"
                                              aria-hidden="true"
                                            ></i>
                                          </span>
                                          <span class="pf-v6-c-label__text">3</span>
                                        </span>
                                      </span>
                                    </li>
                                    <li class="pf-v6-c-label-group__list-item">
                                      <span class="pf-v6-c-label pf-m-teal">
                                        <span class="pf-v6-c-label__content">
                                          <span class="pf-v6-c-label__icon">
                                            <i
                                              class="fas fa-fw fa-bell"
                                              aria-hidden="true"
                                            ></i>
                                          </span>
                                          <span class="pf-v6-c-label__text">3</span>
                                        </span>
                                      </span>
                                    </li>
                                  </ul>
                                </div>
                              </div>
                            </div>
                          </div>
                          <span
                            class="pf-v6-c-notification-drawer__group-toggle-icon"
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
                        </button>
                        <ul
                          class="pf-v6-c-notification-drawer__list"
                          role="list"
                          hidden
                        >
                          <li
                            class="pf-v6-c-notification-drawer__list-item pf-m-hoverable pf-m-danger"
                            tabindex="0"
                          >
                            <div
                              class="pf-v6-c-notification-drawer__list-item-header"
                            >
                              <span
                                class="pf-v6-c-notification-drawer__list-item-header-icon"
                              >
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
                                    d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm-1.5 8a1.5 1.5 0 1 1 3 0v7a1.5 1.5 0 1 1-3 0V9ZM16 25.001a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 25.001Z"
                                  />
                                </svg>
                              </span>
                              <h2
                                class="pf-v6-c-notification-drawer__list-item-header-title"
                              >
                                <span
                                  class="pf-v6-screen-reader"
                                >Danger notification:</span>
                                Critical alert regarding control plane
                              </h2>
                            </div>
                            <div
                              class="pf-v6-c-notification-drawer__list-item-description"
                            >This is a long description to show how the title will wrap if it is long and wraps to multiple lines.</div>
                          </li>
                          <li
                            class="pf-v6-c-notification-drawer__list-item pf-m-hoverable pf-m-warning"
                            tabindex="0"
                          >
                            <div
                              class="pf-v6-c-notification-drawer__list-item-header"
                            >
                              <span
                                class="pf-v6-c-notification-drawer__list-item-header-icon"
                              >
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
                                    d="m31.874 28.514-15.011-27a1.001 1.001 0 0 0-1.748 0l-15.011 27A1 1 0 0 0 .978 30H31a1 1 0 0 0 .874-1.486ZM14.5 12a1.5 1.5 0 0 1 3 0v5a1.5 1.5 0 0 1-3 0v-5ZM16 26.001a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 26.001Z"
                                  />
                                </svg>
                              </span>
                              <h2
                                class="pf-v6-c-notification-drawer__list-item-header-title"
                              >
                                <span
                                  class="pf-v6-screen-reader"
                                >Warning notification:</span>
                                Warning alert
                              </h2>
                            </div>
                            <div
                              class="pf-v6-c-notification-drawer__list-item-description"
                            >This is a warning notification description.</div>
                          </li>
                        </ul>
                      </section>
                    </div>
                  </div>
                </div>
                <!-- inventory -->
                <div class="pf-v6-c-card" id="dashboard-demo-line-chart-card-1">
                  <div class="pf-v6-c-card__header">
                    <div class="pf-v6-c-card__actions pf-m-no-offset">
                      <button
                        class="pf-v6-c-menu-toggle pf-m-text pf-m-plain"
                        type="button"
                        aria-expanded="false"
                        id="dashboard-demo-line-chart-card-1-select-dropdown"
                      >
                        <span class="pf-v6-c-menu-toggle__text">24 hours</span>
                        <span class="pf-v6-c-menu-toggle__controls">
                          <span class="pf-v6-c-menu-toggle__toggle-icon">
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
                                d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
                              />
                            </svg>
                          </span>
                        </span>
                      </button>
                    </div>
                    <div
                      class="pf-v6-c-card__title"
                      id="dashboard-demo-line-chart-card-1-title"
                    >
                      <h2 class="pf-v6-c-title pf-m-xl">Cluster utilizations</h2>
                    </div>
                  </div>
                  <div
                    class="pf-v6-c-card pf-m-plain pf-m-expanded"
                    id="dashboard-demo-line-chart-card-1-group-1"
                  >
                    <div class="pf-v6-c-card__header pf-m-toggle-right">
                      <div class="pf-v6-c-card__header-toggle">
                        <button
                          class="pf-v6-c-button pf-m-plain"
                          id="dashboard-demo-line-chart-card-1-group-1-toggle"
                          type="button"
                          aria-labelledby="dashboard-demo-line-chart-card-1-group-1-title dashboard-demo-line-chart-card-1-group-1-toggle"
                          aria-label="Details"
                        >
                          <span class="pf-v6-c-button__icon pf-m-start">
                            <span class="pf-v6-c-card__header-toggle-icon">
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
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="dashboard-demo-line-chart-card-1-group-1-title"
                        >CPU 1</h2>
                      </div>
                    </div>
                    <div class="pf-v6-c-card__expandable-content">
                      <div class="pf-v6-c-card__body">
                        <div class="pf-v6-l-grid pf-m-gutter">
                          <div class="pf-v6-l-grid pf-m-gutter">
                            <div class="pf-v6-l-grid__item pf-m-4-col-on-md">
                              <div
                                class="pf-v6-l-flex pf-m-column-on-md pf-m-space-items-none-on-md pf-m-justify-content-center-on-md pf-v6-u-h-100-on-md"
                              >
                                <div class="pf-v6-l-flex__item">
                                  <b>Temperature</b>
                                </div>
                                <hr
                                  class="pf-v6-c-divider pf-m-vertical pf-m-inset-sm pf-v6-u-hidden-on-md"
                                />
                                <div class="pf-v6-l-flex__item">
                                  <span>64C</span>
                                </div>
                              </div>
                            </div>
                            <div class="pf-v6-l-grid__item pf-m-8-col-on-md">
                              <div class="pf-v6-l-grid pf-m-gutter">
                                <div class="pf-v6-l-grid__item pf-m-2-col">
                                  <div
                                    class="pf-v6-l-flex pf-m-column pf-m-space-items-none pf-m-align-items-flex-end-on-md"
                                  >
                                    <div class="pf-v6-l-flex__item">100C</div>
                                    <div class="pf-v6-l-flex__item">50C</div>
                                    <div class="pf-v6-l-flex__item">0C</div>
                                  </div>
                                </div>
                                <div class="pf-v6-l-grid__item pf-m-10-col">
                                  <div class="ws-chart">
                                    <img
                                      src="/assets/images/img_line-chart-2.png"
                                      alt="Line chart"
                                    />
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                          <hr class="pf-v6-c-divider pf-v6-u-hidden-on-md" />
                          <div class="pf-v6-l-grid pf-m-gutter">
                            <div class="pf-v6-l-grid__item pf-m-4-col-on-md">
                              <div
                                class="pf-v6-l-flex pf-m-column-on-md pf-m-space-items-none-on-md pf-m-justify-content-center-on-md pf-v6-u-h-100-on-md"
                              >
                                <div class="pf-v6-l-flex__item">
                                  <b>Speed</b>
                                </div>
                                <hr
                                  class="pf-v6-c-divider pf-m-vertical pf-m-inset-sm pf-v6-u-hidden-on-md"
                                />
                                <div class="pf-v6-l-flex__item">
                                  <span>2.3Ghz</span>
                                </div>
                              </div>
                            </div>
                            <div class="pf-v6-l-grid__item pf-m-8-col-on-md">
                              <div class="pf-v6-l-grid pf-m-gutter">
                                <div class="pf-v6-l-grid__item pf-m-2-col">
                                  <div
                                    class="pf-v6-l-flex pf-m-column pf-m-space-items-none pf-m-align-items-flex-end-on-md"
                                  >
                                    <div class="pf-v6-l-flex__item">36hz</div>
                                    <div class="pf-v6-l-flex__item">1.5Ghz</div>
                                    <div class="pf-v6-l-flex__item">0Ghz</div>
                                  </div>
                                </div>
                                <div class="pf-v6-l-grid__item pf-m-10-col">
                                  <div class="ws-chart">
                                    <img
                                      src="/assets/images/img_line-chart-2.png"
                                      alt="Line chart"
                                    />
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div
                    class="pf-v6-c-card pf-m-plain"
                    id="dashboard-demo-line-chart-card-1-group-2"
                  >
                    <div class="pf-v6-c-card__header pf-m-toggle-right">
                      <div class="pf-v6-c-card__header-toggle">
                        <button
                          class="pf-v6-c-button pf-m-plain"
                          id="dashboard-demo-line-chart-card-1-group-2-toggle"
                          type="button"
                          aria-labelledby="dashboard-demo-line-chart-card-1-group-2-title dashboard-demo-line-chart-card-1-group-2-toggle"
                          aria-label="Details"
                        >
                          <span class="pf-v6-c-button__icon pf-m-start">
                            <span class="pf-v6-c-card__header-toggle-icon">
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
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="dashboard-demo-line-chart-card-1-group-2-title"
                        >Pod count</h2>
                      </div>
                    </div>
                  </div>
                  <div
                    class="pf-v6-c-card pf-m-plain"
                    id="dashboard-demo-line-chart-card-1-group-3"
                  >
                    <div class="pf-v6-c-card__header pf-m-toggle-right">
                      <div class="pf-v6-c-card__header-toggle">
                        <button
                          class="pf-v6-c-button pf-m-plain"
                          id="dashboard-demo-line-chart-card-1-group-3-toggle"
                          type="button"
                          aria-labelledby="dashboard-demo-line-chart-card-1-group-3-title dashboard-demo-line-chart-card-1-group-3-toggle"
                          aria-label="Details"
                        >
                          <span class="pf-v6-c-button__icon pf-m-start">
                            <span class="pf-v6-c-card__header-toggle-icon">
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
                      </div>
                      <div class="pf-v6-c-card__title">
                        <h2
                          class="pf-v6-c-card__title-text"
                          id="dashboard-demo-line-chart-card-1-group-3-title"
                        >Memory</h2>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="pf-v6-c-card">
                  <div class="pf-v6-c-card__title">
                    <h2 class="pf-v6-c-title pf-m-xl">Recomendations by severity</h2>
                  </div>
                  <div class="pf-v6-c-card__body">
                    <div class="pf-v6-l-flex pf-m-inline-flex">
                      <div class="pf-v6-l-grid pf-m-gutter pf-m-all-3-col">
                        <div
                          class="pf-v6-l-flex pf-m-column pf-m-space-items-xs pf-m-align-items-center"
                        >
                          <span
                            class="pf-v6-u-font-size-2xl pf-v6-u-primary-color-100"
                          >2</span>
                          <span class="pf-v6-u-font-color-200">Critical</span>
                        </div>
                        <div
                          class="pf-v6-l-flex pf-m-column pf-m-space-items-xs pf-m-align-items-center"
                        >
                          <span
                            class="pf-v6-u-font-size-2xl pf-v6-u-primary-color-100"
                          >5</span>
                          <span class="pf-v6-u-font-color-200">Important</span>
                        </div>
                        <div
                          class="pf-v6-l-flex pf-m-column pf-m-space-items-xs pf-m-align-items-center"
                        >
                          <span
                            class="pf-v6-u-font-size-2xl pf-v6-u-primary-color-100"
                          >7</span>
                          <span class="pf-v6-u-font-color-200">Moderate</span>
                        </div>
                        <div
                          class="pf-v6-l-flex pf-m-column pf-m-space-items-xs pf-m-align-items-center"
                        >
                          <span
                            class="pf-v6-u-font-size-2xl pf-v6-u-primary-color-100"
                          >12</span>
                          <span class="pf-v6-u-font-color-200">Low</span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="pf-v6-c-card__title">
                    <h2 class="pf-v6-c-title pf-m-xl">Recomendations by category</h2>
                  </div>
                  <div class="pf-v6-c-card__body">
                    <img
                      src="/assets/images/img_pie-chart-with-legend.png"
                      alt="Pie chart"
                      width="450"
                    />
                  </div>
                  <div class="pf-v6-c-card__footer">
                    <a href="#">View more</a>
                  </div>
                </div>
              </div>
            </div>
            <div
              class="pf-v6-l-grid__item pf-m-gutter pf-m-4-col-on-lg pf-m-3-col-on-2xl"
              style="--pf-v6-l-grid--item--Order-on-lg:2"
            >
              <div
                class="pf-v6-l-flex pf-m-column pf-m-row-on-md pf-m-column-on-lg"
              >
                <div class="pf-v6-l-flex__item pf-m-flex-1">
                  <div class="pf-v6-c-card" id="dashboard-demo-details-card-1">
                    <div class="pf-v6-c-card__title">
                      <h2 class="pf-v6-c-title pf-m-xl">Details</h2>
                    </div>
                    <div class="pf-v6-c-card__body">
                      <dl class="pf-v6-c-description-list" aria-label="Details">
                        <div class="pf-v6-c-description-list__group">
                          <dt
                            class="pf-v6-c-description-list__term"
                          >Cluster API Address</dt>
                          <dd class="pf-v6-c-description-list__description">
                            <div class="pf-v6-c-description-list__text">
                              <a href="#">https://api1.devcluster.openshift.com</a>
                            </div>
                          </dd>
                        </div>
                        <div class="pf-v6-c-description-list__group">
                          <dt class="pf-v6-c-description-list__term">Cluster ID</dt>
                          <dd class="pf-v6-c-description-list__description">
                            <div
                              class="pf-v6-c-description-list__text"
                            >63b97ac1-b850-41d9-8820-239becde9e86</div>
                          </dd>
                        </div>
                        <div class="pf-v6-c-description-list__group">
                          <dt class="pf-v6-c-description-list__term">Provider</dt>
                          <dd class="pf-v6-c-description-list__description">
                            <div class="pf-v6-c-description-list__text">AWS</div>
                          </dd>
                        </div>
                        <div class="pf-v6-c-description-list__group">
                          <dt
                            class="pf-v6-c-description-list__term"
                          >OpenShift Version</dt>
                          <dd class="pf-v6-c-description-list__description">
                            <div
                              class="pf-v6-c-description-list__text"
                            >4.5.0.ci-2020-06-16-015028</div>
                          </dd>
                        </div>
                        <div class="pf-v6-c-description-list__group">
                          <dt
                            class="pf-v6-c-description-list__term"
                          >Update Channel</dt>
                          <dd class="pf-v6-c-description-list__description">
                            <div
                              class="pf-v6-c-description-list__text"
                            >stable-4.5</div>
                          </dd>
                        </div>
                      </dl>
                    </div>
                    <hr class="pf-v6-c-divider" />
                    <div class="pf-v6-c-card__footer">
                      <a href="#">View Settings</a>
                    </div>
                  </div>
                </div>
                <div class="pf-v6-l-flex__item pf-m-flex-1">
                  <div
                    class="pf-v6-c-card"
                    id="dashboard-demo-data-list-card-1"
                  >
                    <div
                      class="pf-v6-c-card__header pf-v6-u-align-items-flex-start"
                    >
                      <div
                        class="pf-v6-c-card__title"
                        id="dashboard-demo-data-list-card-1-title1"
                      >
                        <h2 class="pf-v6-c-title pf-m-lg">Inventory</h2>
                      </div>
                    </div>
                    <ul
                      class="pf-v6-c-data-list pf-m-grid-none"
                      role="list"
                      aria-label="Simple data list example"
                      id="dashboard-demo-data-list-card-1-data-list"
                    >
                      <li class="pf-v6-c-data-list__item">
                        <div class="pf-v6-c-data-list__item-row">
                          <div class="pf-v6-c-data-list__item-content">
                            <div
                              class="pf-v6-c-data-list__cell"
                              id="dashboard-demo-data-list-card-1-data-list-item-1"
                            >3 Nodes</div>
                            <div
                              class="pf-v6-c-data-list__cell pf-m-no-fill pf-m-align-right"
                            >
                              <a href="#">
                                <div class="pf-v6-l-flex pf-m-space-items-sm">
                                  <span>3</span>
                                  <span class="pf-v6-c-icon">
                                    <span
                                      class="pf-v6-c-icon__content pf-m-success"
                                    >
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
                                          d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                        />
                                      </svg>
                                    </span>
                                  </span>
                                </div>
                              </a>
                            </div>
                          </div>
                        </div>
                      </li>
                      <li class="pf-v6-c-data-list__item">
                        <div class="pf-v6-c-data-list__item-row">
                          <div class="pf-v6-c-data-list__item-content">
                            <div
                              class="pf-v6-c-data-list__cell"
                              id="dashboard-demo-data-list-card-1-data-list-item-2"
                            >8 Disks</div>
                            <div
                              class="pf-v6-c-data-list__cell pf-m-no-fill pf-m-align-right"
                            >
                              <a href="#">
                                <div class="pf-v6-l-flex pf-m-space-items-sm">
                                  <span>8</span>
                                  <span class="pf-v6-c-icon">
                                    <span
                                      class="pf-v6-c-icon__content pf-m-success"
                                    >
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
                                          d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                        />
                                      </svg>
                                    </span>
                                  </span>
                                </div>
                              </a>
                            </div>
                          </div>
                        </div>
                      </li>
                      <li class="pf-v6-c-data-list__item">
                        <div class="pf-v6-c-data-list__item-row">
                          <div class="pf-v6-c-data-list__item-content">
                            <div
                              class="pf-v6-c-data-list__cell"
                              id="dashboard-demo-data-list-card-1-data-list-item-3"
                            >20 Pods</div>
                            <div
                              class="pf-v6-c-data-list__cell pf-m-no-fill pf-m-align-right"
                            >
                              <a href="#">
                                <div class="pf-v6-l-flex pf-m-space-items-sm">
                                  <span>20</span>
                                  <span class="pf-v6-c-icon">
                                    <span
                                      class="pf-v6-c-icon__content pf-m-success"
                                    >
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
                                          d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                        />
                                      </svg>
                                    </span>
                                  </span>
                                </div>
                              </a>
                            </div>
                          </div>
                        </div>
                      </li>
                      <li class="pf-v6-c-data-list__item">
                        <div class="pf-v6-c-data-list__item-row">
                          <div class="pf-v6-c-data-list__item-content">
                            <div
                              class="pf-v6-c-data-list__cell"
                              id="dashboard-demo-data-list-card-1-data-list-item-4"
                            >12 PVs</div>
                            <div
                              class="pf-v6-c-data-list__cell pf-m-no-fill pf-m-align-right"
                            >
                              <a href="#">
                                <div class="pf-v6-l-flex pf-m-space-items-sm">
                                  <span>12</span>
                                  <span class="pf-v6-c-icon">
                                    <span
                                      class="pf-v6-c-icon__content pf-m-success"
                                    >
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
                                          d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                        />
                                      </svg>
                                    </span>
                                  </span>
                                </div>
                              </a>
                            </div>
                          </div>
                        </div>
                      </li>
                      <li class="pf-v6-c-data-list__item">
                        <div class="pf-v6-c-data-list__item-row">
                          <div class="pf-v6-c-data-list__item-content">
                            <div
                              class="pf-v6-c-data-list__cell"
                              id="dashboard-demo-data-list-card-1-data-list-item-5"
                            >18 PVCs</div>
                            <div
                              class="pf-v6-c-data-list__cell pf-m-no-fill pf-m-align-right"
                            >
                              <a href="#">
                                <div class="pf-v6-l-flex pf-m-space-items-sm">
                                  <span>18</span>
                                  <span class="pf-v6-c-icon">
                                    <span
                                      class="pf-v6-c-icon__content pf-m-success"
                                    >
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
                                          d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                        />
                                      </svg>
                                    </span>
                                  </span>
                                </div>
                              </a>
                            </div>
                          </div>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            <div
              class="pf-v6-l-grid__item pf-m-4-col-on-lg pf-m-3-col-on-2xl"
              style="--pf-v6-l-grid--item--Order-on-lg:4"
            >
              <div class="pf-v6-l-flex pf-m-column">
                <div class="pf-v6-c-card" id="dashboard-demo-events-card-1">
                  <div class="pf-v6-c-card__header">
                    <div class="pf-v6-c-card__actions pf-m-no-offset">
                      <button
                        class="pf-v6-c-menu-toggle pf-m-text pf-m-plain"
                        type="button"
                        aria-expanded="false"
                        id="dashboard-demo-events-card-1-select-dropdown"
                      >
                        <span class="pf-v6-c-menu-toggle__text">Status</span>
                        <span class="pf-v6-c-menu-toggle__controls">
                          <span class="pf-v6-c-menu-toggle__toggle-icon">
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
                                d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
                              />
                            </svg>
                          </span>
                        </span>
                      </button>
                    </div>
                    <div
                      class="pf-v6-c-card__title"
                      id="dashboard-demo-events-card-1-title1"
                      style="padding-block-start: 3px;"
                    >
                      <h2 class="pf-v6-c-title pf-m-xl">Events</h2>
                    </div>
                  </div>
                  <div class="pf-v6-c-card__body">
                    <dl
                      class="pf-v6-c-description-list pf-m-compact"
                      aria-label="Events"
                    >
                      <div class="pf-v6-c-description-list__group">
                        <dt class="pf-v6-c-description-list__term">
                          <div class="pf-v6-l-flex pf-m-nowrap">
                            <div class="pf-v6-l-flex__item pf-m-spacer-sm">
                              <span class="pf-v6-c-icon">
                                <span class="pf-v6-c-icon__content pf-m-danger">
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
                                      d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm-1.5 8a1.5 1.5 0 1 1 3 0v7a1.5 1.5 0 1 1-3 0V9ZM16 25.001a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 25.001Z"
                                    />
                                  </svg>
                                </span>
                              </span>
                            </div>
                            <div
                              class="pf-v6-l-flex__item"
                            >Readiness probe failed</div>
                          </div>
                        </dt>
                        <dd class="pf-v6-c-description-list__description">
                          <div
                            class="pf-v6-c-description-list__text"
                          >Readiness probe failed: Get https://10.131.0.7:5000/healthz: dial tcp 10.131.0.7:5000: connect: connection refused</div>
                        </dd>
                        <dd class="pf-v6-c-description-list__description">
                          <div class="pf-v6-c-description-list__text">
                            <time
                              class="pf-v6-u-color-200 pf-v6-u-font-size-sm"
                            >Jun 17, 11:02 am</time>
                          </div>
                        </dd>
                      </div>
                      <div class="pf-v6-c-description-list__group">
                        <dt class="pf-v6-c-description-list__term">
                          <div class="pf-v6-l-flex pf-m-nowrap">
                            <div class="pf-v6-l-flex__item pf-m-spacer-sm">
                              <span class="pf-v6-c-icon">
                                <span
                                  class="pf-v6-c-icon__content pf-m-success"
                                >
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
                                      d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                    />
                                  </svg>
                                </span>
                              </span>
                            </div>
                            <div
                              class="pf-v6-l-flex__item"
                            >Successful assignment</div>
                          </div>
                        </dt>
                        <dd class="pf-v6-c-description-list__description">
                          <div
                            class="pf-v6-c-description-list__text"
                          >Successfully assigned default/example to ip-10-0-130-149.ec2.internal</div>
                        </dd>
                        <dd class="pf-v6-c-description-list__description">
                          <div class="pf-v6-c-description-list__text">
                            <time
                              class="pf-v6-u-color-200 pf-v6-u-font-size-sm"
                            >Jun 17, 11:13 am</time>
                          </div>
                        </dd>
                      </div>
                      <div class="pf-v6-c-description-list__group">
                        <dt class="pf-v6-c-description-list__term">
                          <div class="pf-v6-l-flex pf-m-nowrap">
                            <div class="pf-v6-l-flex__item pf-m-spacer-sm">
                              <svg
                                class="pf-v6-c-spinner pf-m-md"
                                role="progressbar"
                                viewBox="0 0 100 100"
                                aria-label="Loading"
                              >
                                <circle
                                  class="pf-v6-c-spinner__path"
                                  cx="50"
                                  cy="50"
                                  r="45"
                                  fill="none"
                                />
                              </svg>
                            </div>
                            <div class="pf-v6-l-flex__item">Pulling image</div>
                          </div>
                        </dt>
                        <dd class="pf-v6-c-description-list__description">
                          <div
                            class="pf-v6-c-description-list__text"
                          >Pulling image "openshift/hello-openshift"</div>
                        </dd>
                        <dd class="pf-v6-c-description-list__description">
                          <div class="pf-v6-c-description-list__text">
                            <time
                              class="pf-v6-u-color-200 pf-v6-u-font-size-sm"
                            >Jun 17, 10:59 am</time>
                          </div>
                        </dd>
                      </div>
                      <div class="pf-v6-c-description-list__group">
                        <dt class="pf-v6-c-description-list__term">
                          <div class="pf-v6-l-flex pf-m-nowrap">
                            <div class="pf-v6-l-flex__item pf-m-spacer-sm">
                              <span class="pf-v6-c-icon">
                                <span
                                  class="pf-v6-c-icon__content pf-m-success"
                                >
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
                                      d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                    />
                                  </svg>
                                </span>
                              </span>
                            </div>
                            <div class="pf-v6-l-flex__item">Created container</div>
                          </div>
                        </dt>
                        <dd class="pf-v6-c-description-list__description">
                          <div
                            class="pf-v6-c-description-list__text"
                          >Created container hello-openshift</div>
                        </dd>
                        <dd class="pf-v6-c-description-list__description">
                          <div class="pf-v6-c-description-list__text">
                            <time
                              class="pf-v6-u-color-200 pf-v6-u-font-size-sm"
                            >Jun 17, 10:45 am</time>
                          </div>
                        </dd>
                      </div>

                      <div class="pf-v6-c-description-list__group">
                        <dt class="pf-v6-c-description-list__term">
                          <div class="pf-v6-l-flex pf-m-nowrap">
                            <div class="pf-v6-l-flex__item pf-m-spacer-sm">
                              <span class="pf-v6-c-icon">
                                <span
                                  class="pf-v6-c-icon__content pf-m-warning"
                                >
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
                                      d="m31.874 28.514-15.011-27a1.001 1.001 0 0 0-1.748 0l-15.011 27A1 1 0 0 0 .978 30H31a1 1 0 0 0 .874-1.486ZM14.5 12a1.5 1.5 0 0 1 3 0v5a1.5 1.5 0 0 1-3 0v-5ZM16 26.001a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 26.001Z"
                                    />
                                  </svg>
                                </span>
                              </span>
                            </div>
                            <div
                              class="pf-v6-l-flex__item"
                            >CPU utilitization over 50%</div>
                          </div>
                        </dt>
                        <dd class="pf-v6-c-description-list__description">
                          <div
                            class="pf-v6-c-description-list__text"
                          >Migrated 2 pods to other hosts</div>
                        </dd>
                        <dd class="pf-v6-c-description-list__description">
                          <div class="pf-v6-c-description-list__text">
                            <time
                              class="pf-v6-u-color-200 pf-v6-u-font-size-sm"
                            >Jun 17, 10:33 am</time>
                          </div>
                        </dd>
                      </div>

                      <div class="pf-v6-c-description-list__group">
                        <dt class="pf-v6-c-description-list__term">
                          <div class="pf-v6-l-flex pf-m-nowrap">
                            <div class="pf-v6-l-flex__item pf-m-spacer-sm">
                              <span class="pf-v6-c-icon">
                                <span class="pf-v6-c-icon__content pf-m-danger">
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
                                      d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm-1.5 8a1.5 1.5 0 1 1 3 0v7a1.5 1.5 0 1 1-3 0V9ZM16 25.001a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 25.001Z"
                                    />
                                  </svg>
                                </span>
                              </span>
                            </div>
                            <div class="pf-v6-l-flex__item">Rook-osd-10-328949</div>
                          </div>
                        </dt>
                        <dd class="pf-v6-c-description-list__description">
                          <div
                            class="pf-v6-c-description-list__text"
                          >Rebuild initiated as Disk 5 failed</div>
                        </dd>
                        <dd class="pf-v6-c-description-list__description">
                          <div class="pf-v6-c-description-list__text">
                            <time
                              class="pf-v6-u-color-200 pf-v6-u-font-size-sm"
                            >Jun 17, 10:33 am</time>
                          </div>
                        </dd>
                      </div>

                      <div class="pf-v6-c-description-list__group">
                        <dt class="pf-v6-c-description-list__term">
                          <div class="pf-v6-l-flex pf-m-nowrap">
                            <div class="pf-v6-l-flex__item pf-m-spacer-sm">
                              <span class="pf-v6-c-icon">
                                <span
                                  class="pf-v6-c-icon__content pf-m-success"
                                >
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
                                      d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                    />
                                  </svg>
                                </span>
                              </span>
                            </div>
                            <div class="pf-v6-l-flex__item">Created container</div>
                          </div>
                        </dt>
                        <dd class="pf-v6-c-description-list__description">
                          <div
                            class="pf-v6-c-description-list__text"
                          >Created container hello-openshift-123</div>
                        </dd>
                        <dd class="pf-v6-c-description-list__description">
                          <div class="pf-v6-c-description-list__text">
                            <time
                              class="pf-v6-u-color-200 pf-v6-u-font-size-sm"
                            >Jun 17, 10:31 am</time>
                          </div>
                        </dd>
                      </div>

                      <div class="pf-v6-c-description-list__group">
                        <dt class="pf-v6-c-description-list__term">
                          <div class="pf-v6-l-flex pf-m-nowrap">
                            <div class="pf-v6-l-flex__item pf-m-spacer-sm">
                              <span class="pf-v6-c-icon">
                                <span
                                  class="pf-v6-c-icon__content pf-m-success"
                                >
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
                                      d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
                                    />
                                  </svg>
                                </span>
                              </span>
                            </div>
                            <div class="pf-v6-l-flex__item">Created container</div>
                          </div>
                        </dt>
                        <dd class="pf-v6-c-description-list__description">
                          <div
                            class="pf-v6-c-description-list__text"
                          >Created container hello-openshift-456</div>
                        </dd>
                        <dd class="pf-v6-c-description-list__description">
                          <div class="pf-v6-c-description-list__text">
                            <time
                              class="pf-v6-u-color-200 pf-v6-u-font-size-sm"
                            >Jun 17, 10:30 am</time>
                          </div>
                        </dd>
                      </div>
                    </dl>
                  </div>
                  <hr class="pf-v6-c-divider" />
                  <div class="pf-v6-c-card__footer">
                    <a href="#">View all events</a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</div>

```
